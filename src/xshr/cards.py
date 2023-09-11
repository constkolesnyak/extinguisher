from enum import CONTINUOUS, Flag, IntEnum, auto, unique, verify
from typing import Optional, Self

import attrs


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

    # todo repr?

    def __str__(self) -> str:
        return ''  # todo

    @classmethod
    def from_str(cls, rank: str) -> Self:
        ...  # todo


@unique
class Suit(Flag):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()
    RED = HEARTS | DIAMONDS
    BLACK = CLUBS | SPADES

    # todo repr?

    def __str__(self) -> str:
        return ''  # todo

    @classmethod
    def from_str(cls, suit: str) -> Self:
        ...  # todo


_JOKER_STR = '\U0001fa85'  # 🪅


@attrs.define(frozen=True)
class Card:
    rank: Optional[Rank] = None
    suit: Optional[Suit] = None
    joker_id: Optional[int] = None

    @property
    def is_joker(self) -> bool:
        return self.joker_id is not None

    def __str__(self) -> str:
        return _JOKER_STR if self.is_joker else f'{self.rank}{self.suit}'


if __name__ == '__main__':
    ...
