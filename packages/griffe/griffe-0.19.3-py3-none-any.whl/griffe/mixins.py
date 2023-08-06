"""This module contains some mixins classes about accessing and setting members."""

from __future__ import annotations

from contextlib import suppress
from typing import Any, Sequence

from griffe.logger import get_logger
from griffe.merger import merge_stubs

logger = get_logger(__name__)


class GetMembersMixin:
    """This mixin adds a `__getitem__` method to a class.

    It makes it easier to access members of an object.
    The method expects a `members` attribute/property to be available on the instance.
    """

    def __getitem__(self, key: str | Sequence[str]) -> Any:
        parts = _get_parts(key)
        if len(parts) == 1:
            return self.members[parts[0]]  # type: ignore[attr-defined]
        return self.members[parts[0]][parts[1:]]  # type: ignore[attr-defined]


def _get_parts(key: str | Sequence[str]) -> Sequence[str]:
    if isinstance(key, str):
        if not key:
            raise ValueError("Empty strings are not supported")
        parts = key.split(".")
    else:
        parts = list(key)
    if not parts:
        raise ValueError("Empty tuples are not supported")
    return parts


class DelMembersMixin:
    """This mixin adds a `__delitem__` method to a class."""

    def __delitem__(self, key: str | Sequence[str]) -> None:  # noqa: WPS603
        parts = _get_parts(key)
        if len(parts) == 1:
            name = parts[0]
            del self.members[name]  # type: ignore[attr-defined]  # noqa: WPS420
        else:
            del self.members[parts[0]][parts[1:]]  # type: ignore[attr-defined]  # noqa: WPS420


class SetMembersMixin(DelMembersMixin):
    """This mixin adds a `__setitem__` method to a class.

    It makes it easier to set members of an object.
    The method expects a `members` attribute/property to be available on the instance.
    Each time a member is set, its `parent` attribute is set as well.
    """

    def __setitem__(self, key: str | Sequence[str], value) -> None:  # noqa: WPS231
        parts = _get_parts(key)
        if len(parts) == 1:
            name = parts[0]
            if name in self.members:  # type: ignore[attr-defined]
                member = self.members[name]  # type: ignore[attr-defined]
                if not member.is_alias:
                    # when reassigning a module to an existing one,
                    # try to merge them as one regular and one stubs module
                    # (implicit support for .pyi modules)
                    if member.is_module and value.is_module:
                        logger.debug(f"Trying to merge {member.filepath} and {value.filepath}")
                        with suppress(ValueError):
                            value = merge_stubs(member, value)
                    for alias in member.aliases.values():
                        alias.target = value
            self.members[name] = value  # type: ignore[attr-defined]
            value.parent = self
        else:
            self.members[parts[0]][parts[1:]] = value  # type: ignore[attr-defined]


class SetCollectionMembersMixin(DelMembersMixin):
    """This mixin adds a `__setitem__` method to a class.

    It makes it easier to set members of an object.
    The method expects a `members` attribute/property to be available on the instance.
    Each time a member is set, its `_modules_collection` attribute is set as well.
    """

    def __setitem__(self, key: str | Sequence[str], value):
        parts = _get_parts(key)
        if len(parts) == 1:
            name = parts[0]
            if name in self.members:  # type: ignore[attr-defined]
                for alias in self.members[name].aliases.values():  # type: ignore[attr-defined]
                    alias.target = value
            self.members[name] = value  # type: ignore[attr-defined]
            value._modules_collection = self  # noqa: WPS437
        else:
            self.members[parts[0]][parts[1:]] = value  # type: ignore[attr-defined]


class ObjectAliasMixin:
    """A mixin for methods that appear both in objects and aliases, unchanged."""

    def is_exported(self, explicitely: bool = True) -> bool:
        """Tell if this object/alias is implicitely exported by its parent.

        Parameters:
            explicitely: Whether to only return True when `__all__` is defined.

        Returns:
            True or False.
        """
        return self.parent.member_is_exported(self, explicitely=explicitely)  # type: ignore[attr-defined]

    @property
    def is_explicitely_exported(self) -> bool:
        """Tell if this object/alias is explicitely exported by its parent.

        Returns:
            True or False.
        """
        return self.is_exported(explicitely=True)

    @property
    def is_implicitely_exported(self) -> bool:
        """Tell if this object/alias is implicitely exported by its parent.

        Returns:
            True or False.
        """
        return self.parent.exports is None  # type: ignore[attr-defined]
