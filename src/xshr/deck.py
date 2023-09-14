from itertools import chain, product
from pprint import pprint
from random import SystemRandom

from xshr.card import Card, Rank, Suit

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
