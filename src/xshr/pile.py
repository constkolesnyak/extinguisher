import operator
from functools import reduce
from pprint import pprint
from typing import Iterator

import attrs

from xshr.card import Card, Mark, Suit
from xshr.deck import CARD_GROUPS, JOKERS


@attrs.define(frozen=True)
class Pile:
    _cards: frozenset[Card] = attrs.field(converter=frozenset)

    @property
    def jokers(self) -> frozenset[Card]:
        return self._cards & JOKERS

    def find(self, mark: Mark) -> frozenset[Card]:
        if isinstance(mark, Suit):
            return reduce(operator.or_, (CARD_GROUPS[suit] for suit in mark))
        return self._cards & CARD_GROUPS[mark]

    def __iter__(self) -> Iterator[Card]:
        return iter(self._cards)
