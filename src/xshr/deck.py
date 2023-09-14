from collections import defaultdict
from itertools import chain, product
from pprint import pprint
from random import SystemRandom

from xshr.card import Card, Mark, Rank, Suit

_JOKERS_QUANTITY = 4
JOKERS = set(
    map(
        Card.from_iterable,
        chain(
            ((None, Suit.RED, joker_id) for joker_id in range(_JOKERS_QUANTITY // 2)),
            (
                (None, Suit.BLACK, joker_id)
                for joker_id in range(_JOKERS_QUANTITY // 2, _JOKERS_QUANTITY)
            ),
        ),
    )
)

DECK = tuple(chain(map(Card.from_iterable, product(Rank, Suit)), JOKERS))


def new_shuffled_deck() -> list[Card]:
    return SystemRandom().sample(DECK, len(DECK))


def _init_card_groups() -> dict[Mark, set[Card]]:
    card_groups: defaultdict[Mark, set[Card]] = defaultdict(set)

    for _card in DECK[:-_JOKERS_QUANTITY]:
        for _mark in _card.marks:
            card_groups[_mark].add(_card)

    return dict(card_groups)


CARD_GROUPS: dict[Mark, set[Card]] = _init_card_groups()
