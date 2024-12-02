from collections import Counter

# Cards are ordered by decreasing strength
CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def get_deck() -> dict[str, int]:
    """Return the deck.

    Keys as hands, and values as ranks.

    :return dict[str, int]: deck
    """
    deck = {}
    for hand in lines:
        cards, rank = hand[0].split()
        deck[cards] = int(rank)
    return deck


def get_ranking() -> dict[int, set]:
    """Return the ranking of all hands in the deck.

    Keys as rank (e.g. 1), and values as hands in that rank (e.g. '222J5').
    Using a set assumes that all hands in the deck are unique.

    Every hand is exactly one type. From strongest to weakest, they are:
        - `Five of a kind`, where all five cards have the same label: AAAAA
        - `Four of a kind`, where four cards have the same label and one card has a different label: AA8AA
        - `Full house`, where three cards have the same label, and the remaining two cards share a different label: 23332
        - `Three of a kind`, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        - `Two pair`, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        - `One pair`, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        - `High card`, where all cards' labels are distinct: 23456

    :return dict[int, set]: ranking
    """
    ranking = {k: set() for k in range(7)}
    for hand in deck.keys():
        # Replace jokers by highest occuring card
        has_jokers = Counter(hand).get("J")

        if has_jokers:
            # Hand with at least 1 joker card, and at most 5 joker cards (e.g. 'JJK23')
            if 5 > has_jokers >= 1:
                without_jokers = Counter(hand)
                without_jokers.pop("J")
                h = hand.replace("J", max(without_jokers, key=without_jokers.get))

            # Edge case: 'JJJJJ'
            elif has_jokers == 5:
                h = hand
                pass
        else:
            h = hand

        # Match hand types to ranks
        hand_type = sorted(Counter(h).values())
        match hand_type:
            case [1, 1, 1, 1, 1]:
                ranking[0].add(hand)
            case [1, 1, 1, 2]:
                ranking[1].add(hand)
            case [1, 2, 2]:
                ranking[2].add(hand)
            case [1, 1, 3]:
                ranking[3].add(hand)
            case [2, 3]:
                ranking[4].add(hand)
            case [1, 4]:
                ranking[5].add(hand)
            case [5]:
                ranking[6].add(hand)
    return ranking


def get_winnings_with_joker() -> int:
    """Return the total winnings (handles joker cards).

    :return int: total winnings
    """

    def sort_hands(hands: list, idx: int) -> None:
        """Recursive function to append hands by score to their respective rank.

        :param list hands: current hands
        :param int idx: current index (e.g. index 2 of 'A26KK' is '2')
        """
        # Sort hands by char at index
        sorting = {hand: CARDS.index(hand[idx]) for hand in hands}

        # Get lowest-scoring hands first
        lowest_scoring = [
            hand for hand in hands if sorting[hand] == max(sorting.values())
        ]

        # Get lowest-scoring hands at next index
        next_sorting = {hand: CARDS.index(hand[idx + 1]) for hand in lowest_scoring}

        # Check if can score based on next index (i.e. if only 1 result)
        cannot_sort_next = any([x > 1 for x in Counter(next_sorting.values()).values()])

        if cannot_sort_next:
            sort_hands(lowest_scoring, idx + 1)

        else:
            sorting = {hand: CARDS.index(hand[idx + 1]) for hand in lowest_scoring}
            sorted_dict = dict(
                sorted(sorting.items(), key=lambda item: item[1], reverse=True)
            )
            for hand in sorted_dict:
                sorted_hands.append(hand)
                deck_hands.remove(hand)

            # If there are still hands in the deck, continue sorting
            if deck_hands:
                sort_hands(deck_hands, 0)

    for rank, hands in ranking.items():
        deck_hands = ranking[rank]
        sorted_hands = []

        # Reset index to 0 and sort next rank
        idx = 0
        sort_hands(hands, idx)
        ranking[rank] = sorted_hands

    flat_deck = [y for x in ranking.values() for y in x if x]
    scores = [deck[hand] * (rank + 1) for rank, hand in enumerate(flat_deck)]
    result = sum(scores)
    return result


if __name__ == "__main__":
    with open("2023/day07/input.txt", "r") as file:
        lines = file.read().splitlines()
        lines = [x.split(":") for x in lines]

    deck = get_deck()
    ranking = get_ranking()
    result = get_winnings_with_joker()
    print(f"Total winnings (with joker cards): {result}")
