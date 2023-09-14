from collections import defaultdict
from functools import partial
from itertools import chain, product, starmap
from pprint import pprint
from random import SystemRandom

from xshr.card import Card, Mark, Rank, Suit

_JOKERS_QUANTITY = 4


def _init_jokers(quantity: int = _JOKERS_QUANTITY):
    red = ((Suit.RED, id_) for id_ in range(quantity // 2))
    black = ((Suit.BLACK, id_) for id_ in range(quantity // 2, jokers))

    return frozenset(starmap(partial(Card, None), chain(red, black)))


JOKERS = _init_jokers()

DECK = tuple(chain(starmap(Card, product(Rank, Suit)), JOKERS))


def new_shuffled_deck() -> list[Card]:
    return SystemRandom().sample(DECK, len(DECK))


def _init_card_groups() -> dict[Mark, set[Card]]:
    card_groups: defaultdict[Mark, set[Card]] = defaultdict(set)

    for _card in DECK[:-_JOKERS_QUANTITY]:
        for _mark in _card.marks:
            card_groups[_mark].add(_card)

    return dict(card_groups)


CARD_GROUPS: dict[Mark, set[Card]] = _init_card_groups()
