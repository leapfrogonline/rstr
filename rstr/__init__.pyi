import re
from typing import Any, Callable, List, MutableSequence, Optional, Protocol, TypeVar, Union

_T = TypeVar('_T')


class _Random(Protocol):
    """Partial interface of the random module needed for the rstr library."""

    def randint(self, a: int, b: int) -> int:
        ...

    def choice(self, seq: Sequence[_T]) -> _T:
        ...

    def shuffle(
        self,
        x: MutableSequence[Any],
        random: Optional[Callable[[], float]] = ...,
    ) -> None:
        ...


class _PartialRstrFunc(Protocol):

    def __call__(
        self,
        start_range: Optional[int] = ...,
        end_range: Optional[int] = ...,
        include: str = ...,
        exclude: str = ...,
    ) -> str:
        ...


class Rstr:

    def __init__(self, _random: _Random = ..., **alphabets: str) -> None:
        ...

    def __getattr__(self, attr: str) -> _PartialRstrFunc:
        ...

    def add_alphabet(self, alpha_name: str, characters: str) -> None:
        ...

    def sample_wr(self, population: Sequence[str], k: int) -> List[str]:
        ...

    def rstr(
        self,
        alphabet: Iterable[str],
        start_range: Optional[int] = ...,
        end_range: Optional[int] = ...,
        include: Sequence[str] = ...,
        exclude: Sequence[str] = ...,
    ) -> str:
        ...

    def xeger(self, string_or_regex: Union[str, re.Pattern]) -> str:
        ...


def rstr(
    alphabet: Iterable[str],
    start_range: Optional[int] = ...,
    end_range: Optional[int] = ...,
    include: Sequence[str] = ...,
    exclude: Sequence[str] = ...,
) -> str:
    ...


def xeger(string_or_regex: Union[str, re.Pattern]) -> str:
    ...


printable: _PartialRstrFunc
letters: _PartialRstrFunc
uppercase: _PartialRstrFunc
lowercase: _PartialRstrFunc
digits: _PartialRstrFunc
punctuation: _PartialRstrFunc
nondigits: _PartialRstrFunc
nonletters: _PartialRstrFunc
whitespace: _PartialRstrFunc
nonwhitespace: _PartialRstrFunc
normal: _PartialRstrFunc
word: _PartialRstrFunc
nonword: _PartialRstrFunc
unambiguous: _PartialRstrFunc
postalsafe: _PartialRstrFunc
urlsafe: _PartialRstrFunc
domainsafe: _PartialRstrFunc
