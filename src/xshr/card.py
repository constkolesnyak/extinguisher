from enum import CONTINUOUS, Flag, IntEnum, auto, unique, verify
from itertools import chain, dropwhile, takewhile
from pprint import pprint
from typing import Callable, Optional, Self

import attrs
from bidict import bidict


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
        # if self not in _RANK_TO_STR:
        #     raise  # todo
        return _RANK_TO_STR[self]

    @classmethod
    def from_str(cls, suit: str) -> Self:
        # if self not in _RANK_TO_STR.inv:
        #     raise  # todo
        return _RANK_TO_STR.inv[suit]


@unique
class Suit(Flag):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()
    RED = HEARTS | DIAMONDS
    BLACK = CLUBS | SPADES
    ANY = RED | BLACK

    def __str__(self) -> str:
        # if self not in _SUIT_TO_STR:
        #     raise  # todo
        return _SUIT_TO_STR[self]

    @classmethod
    def from_str(cls, suit: str) -> Self:
        # if self not in _SUIT_TO_STR.inv:
        #     raise  # todo
        return _SUIT_TO_STR.inv[suit]


Mark = Rank | Suit

_is_not_jack: Callable[[Rank], bool] = lambda rank: rank != Rank.JACK

_RANK_TO_STR: bidict[Rank, str] = bidict(
    zip(
        Rank,
        chain(
            (str(rank.value) for rank in takewhile(_is_not_jack, Rank)),
            (rank.name[0].upper() for rank in dropwhile(_is_not_jack, Rank)),
        ),
        strict=True,
    )
)

_SUIT_TO_STR: bidict[Suit, str] = bidict(
    {
        Suit.HEARTS: '\U00002665',  # ♥
        Suit.DIAMONDS: '\U00002666',  # ♦
        Suit.CLUBS: '\U00002663',  # ♣
        Suit.SPADES: '\U00002660',  # ♠
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

    # @property #todo?
    # def marks(self) -> tuple[Mark]:
    #     return self.rank, self.suit

    def __str__(self) -> str:
        return _JOKER_STR if self.is_joker else f'{self.rank}{self.suit}'


if __name__ == '__main__':
    ...
