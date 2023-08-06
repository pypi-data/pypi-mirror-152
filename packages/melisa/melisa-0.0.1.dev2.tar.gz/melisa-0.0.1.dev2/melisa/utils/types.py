# Copyright MelisaDev 2022 - Present
# Full MIT License can be found in `LICENSE.txt` at the project root.

from __future__ import annotations

from sys import modules
from typing import TypeVar, Callable, Coroutine, Any, Union


class UndefinedType:
    """The type of the `UNDEFINED`."""

    def __bool__(self):
        return False

    def __copy__(self):
        return self

    def __getstate__(self):
        return False

    def __repr__(self) -> str:
        return "<UNDEFINED>"

    def __reduce__(self) -> str:
        return "<UNDEFINED>"

    def __str__(self) -> str:
        return "<UNDEFINED>"


UNDEFINED = UndefinedType()

T = TypeVar("T")

Coro = TypeVar("Coro", bound=Callable[..., Coroutine[Any, Any, Any]])

APINullable = Union[T, UndefinedType, None]


class Singleton(type):
    # Thanks to this stackoverflow answer (method 3):
    # https://stackoverflow.com/q/6760685/12668716
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TypeCache(metaclass=Singleton):
    # Thanks Pincer Devs. This class is from the Pincer Library.
    cache = {}

    def __init__(self):
        lcp = modules.copy()
        for module in lcp:
            if not module.startswith("melisa"):
                continue

            TypeCache.cache.update(lcp[module].__dict__)
