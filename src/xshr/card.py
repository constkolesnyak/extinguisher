from enum import CONTINUOUS, Flag, IntEnum, auto, unique, verify
from itertools import chain
from pprint import pprint
from typing import Callable, Optional, Self

import attrs
from bidict import bidict
from more_itertools import split_before


class InvalidMarkError(Exception):
    pass


@unique
@verify(CONTINUOUS)
class Rank(IntEnum):
    TWO = 2
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()

    def __str__(self) -> str:
        return _RANK_TO_STR[self]

    @classmethod
    def from_str(cls, rank: str) -> Self:
        try:
            return _RANK_TO_STR.inv[rank]
        except KeyError as exc:
            raise InvalidMarkError(f"'{rank}' is an invalid rank") from exc


@unique
class Suit(Flag):
    CLUBS = auto()
    HEARTS = auto()
    SPADES = auto()
    DIAMONDS = auto()

    RED = HEARTS | DIAMONDS
    BLACK = CLUBS | SPADES
    ANY = RED | BLACK

    def __str__(self) -> str:
        return _SUIT_TO_STR[self]

    @classmethod
    def from_str(cls, suit: str) -> Self:
        try:
            return _SUIT_TO_STR.inv[suit]
        except KeyError as exc:
            raise InvalidMarkError(f"'{suit}' is an invalid suit") from exc


Mark = Optional[Rank | Suit]


def _init_rank_to_str() -> bidict[Rank, str]:
    is_jack: Callable[[Rank], bool] = lambda rank: rank == Rank.JACK
    rank_numbers, rank_words = split_before(Rank, is_jack)

    strings_of_ranks = chain(
        (str(rank.value) for rank in rank_numbers),
        (rank.name[0].upper() for rank in rank_words),
    )

    return bidict(
        zip(
            Rank,
            strings_of_ranks,
            strict=True,
        )
    )


_RANK_TO_STR: bidict[Rank, str] = _init_rank_to_str()
_SUIT_TO_STR: bidict[Suit, str] = bidict(
    {
        Suit.CLUBS: '\U00002663',  # ♣
        Suit.HEARTS: '\U00002665',  # ♥
        Suit.SPADES: '\U00002660',  # ♠
        Suit.DIAMONDS: '\U00002666',  # ♦
    }
)

_JOKER_STR = '\U0001fa85'  # 🪅


@attrs.define(frozen=True)
class Card:
    rank: Optional[Rank] = None
    suit: Optional[Suit] = None
    joker_id: Optional[int] = None

    def __attrs_post_init__(self) -> None:
        assert self.suit is not None
        assert (self.rank is None) ^ (self.joker_id is None)

    @property
    def is_joker(self) -> bool:
        return self.joker_id is not None

    @property
    def marks(self) -> tuple[Mark, Mark]:
        return self.rank, self.suit

    def __str__(self) -> str:
        return _JOKER_STR if self.is_joker else f'{self.rank}{self.suit}'


if __name__ == '__main__':
    ...
