"""
Define hooks that can trigger user actions.
"""

import asyncio
from collections import defaultdict
from enum import Enum
from itertools import chain
from typing import Any, Callable, Coroutine, Dict, Generic, Optional, Set, Tuple, TypeVar


class Event:
    """Base class for event system."""

    pass


Evt = TypeVar("Evt", bound=Event)
T = TypeVar("T")


class NullEvent(Event):
    """For debugging"""

    __slots__ = ()

    def __getattribute__(self, __name: str):
        try:
            return super().__getattribute__(__name)
        except AttributeError:
            raise AssertionError("call `o.register_hook` before accessing `o.hook`")

    def __repr__(self) -> str:
        return "NullEvent()"


class Emittable(Generic[Evt]):
    """An object has some event to trigger."""

    hook: Evt = NullEvent()  # type: ignore
    _tasks: Dict[str, Set[asyncio.Task]]
    _loop: asyncio.AbstractEventLoop

    def __init__(self) -> None:
        self._tasks = defaultdict(set)
        self._loop = asyncio.get_event_loop()

    def register_hook(self, hook: Evt):
        assert not isinstance(hook, NullEvent)
        self.hook = hook

    def add_hook_ref(self, hook_cls, coro):
        # type: (str, Coroutine[Any, Any, T]) -> asyncio.Task[T]
        # NOTE: asyncio.Task becomes generic since py39
        task = self._loop.create_task(coro)
        self._tasks[hook_cls].add(task)
        task.add_done_callback(lambda t: self._tasks[hook_cls].remove(t))
        return task

    async def wait(
        self,
        *hook_cls: str,
        timeout: Optional[float] = None,
    ) -> Tuple[Set[asyncio.Task], Set[asyncio.Task]]:
        """Wait for all task in the specific task set(s).

        :param timeout: timeout, defaults to None
        :type timeout: float, optional
        :return: done, pending

        .. note::
            If `timeout` is None, this method will loop until all tasks in the set(s) are done.
            That means if other tasks are added during awaiting, the added task will be waited as well.

        .. seealso:: :meth:`asyncio.wait`
        """
        s = set()
        for i in hook_cls:
            s.update(self._tasks[i])
        if not s:
            return set(), set()
        r = await asyncio.wait(s, timeout=timeout)
        if timeout is None and any(self._tasks[i] for i in hook_cls):
            # await potential new tasks in these sets, only if no timeout.
            r2 = await Emittable.wait(self, *hook_cls)
            return set(chain(r[0], r2[0])), set()
        return r

    def clear(self, *hook_cls: str, cancel: bool = True):
        """Clear the given task sets

        :param hook_cls: task class names
        :param cancel: Cancel the task if a set is not empty, defaults to True. Else will just clear the ref.
        """
        for i in hook_cls:
            s = self._tasks[i]
            if s and not cancel:
                s.clear()
                continue
            while s:
                t = s.pop()
                t.cancel()


class LoginMethod(str, Enum):
    qr = "qr"
    up = "up"
    mixed = "mixed"


class LoginEvent(Event):
    """Defines usual events happens during login."""

    async def LoginFailed(self, meth: LoginMethod, msg: Optional[str] = None):
        """Will be emitted on login failed.

        :param meth: indicate what login method this login attempt used
        :param msg: Err msg, defaults to None.
        """
        raise NotImplementedError

    async def LoginSuccess(self, meth: LoginMethod):
        """Will be emitted after login success.

        :param meth: indicate what login method this login attempt used
        """
        pass


class QREvent(LoginEvent):
    """Defines usual events happens during QR login."""

    cancel: Optional[Callable[[], Coroutine[Any, Any, None]]] = None
    resend: Optional[Callable[[], Coroutine[Any, Any, None]]] = None

    async def QrFetched(self, png: bytes, renew: bool = False):
        """Will be called on new QR code bytes are fetched. Means this will be triggered on:

        1. QR login start
        2. QR expired
        3. QR is refreshed

        :param png: QR bytes (png format)
        :param renew: this QR is a refreshed QR, defaults to False

        .. deprecated:: ?

            Develpers had better not rely on the parameter `renew`.
            Maintaining the state by yourself is not difficult.
        """
        pass

    async def QrFailed(self, msg: Optional[str] = None):
        """QR login failed.

        :param msg: Error msg, defaults to None.

        .. deprecated:: 0.9.0
        """
        await self.LoginFailed(LoginMethod.qr, msg)

    async def QrSucceess(self):
        """QR login success.

        .. deprecated:: 0.9.0
        """
        await self.LoginSuccess(LoginMethod.qr)


class UPEvent(LoginEvent):
    async def DynamicCode(self) -> int:
        """Get dynamic code from sms. A sms with dynamic code will be sent to user's mobile before
        this event is emitted. This hook should return that code (from user input, etc.).

        :return: dynamic code in sms
        """
        return 0
