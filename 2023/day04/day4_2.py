import re


def get_copies(scratchcard: str) -> tuple[int, range]:
    """Return the copies per scratchcard.

    :param str scratchcard: scratchcard (e.g. `Card   1: 69 12 75 ... | 83 63 56 ...`)
    :return tuple: card number (e.g. `1`) and copies of cards (e.g. `range(2, 12)`)
    """
    result = re.match(pattern, scratchcard)
    card, own, win = [[*map(int, x.split())] for x in result.groups()]
    card = card.pop()
    intersection = len(set(own) & set(win))

    # Add copies of cards based on intersection
    copies = range(card + 1, card + intersection + 1)

    # Initialise cards counter
    cards[card] = 1

    return card, copies


def get_scratchcards(card_copies: range) -> None:
    """Update the cards dictionary recursively.

    :param range card_copies: range of scratchcards to iterate over
    """
    for card in card_copies:
        cards[card] += 1
        if copies[card]:
            get_scratchcards(copies[card])


if __name__ == "__main__":
    with open("2023/day04/input.txt", "r") as file:
        data = file.read().splitlines()

    pattern = r"Card\s+(\d+):(?:\s+)((?:\d+\s*)+)\s\|(?:\s+)((?:\d+\s*)+)"
    cards = {}
    copies = {card: copies for card, copies in map(lambda x: get_copies(x), data)}

    for card_copies in copies.values():
        get_scratchcards(card_copies)

    print(f"Total number of scratchcards: {sum(cards.values())}")
