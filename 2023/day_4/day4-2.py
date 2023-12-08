import re


def get_copies(pattern: str) -> dict:
    """Return the copies per scratchcard.

    For example, for cards 1 and 2:
    ```py
    copies = {
        1: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        2: [3, 4, 5, 6, 7, 8, 9, 10]
    }
    ```

    :param str pattern: regex pattern
    :return dict: total number of cards
    """
    copies = {}
    for string in strings:
        res = re.match(pattern, string)
        if res:
            # Preprocessing (as in day4-1.py)
            numbers_str = list(map(lambda x: re.split(r"\s+", x), res.groups()))
            numbers_int = list(map(lambda x: [int(y) for y in x], numbers_str))
            card_number = numbers_int[0][0]
            own_numbers = set(numbers_int[1])
            win_numbers = set(numbers_int[2])
            intersection = len(own_numbers & win_numbers)

            # Add copies of cards based on intersection
            next_cards = list(range(card_number + 1, card_number + intersection + 1))

            # Populate copies per scratchcard
            try:
                copies[card_number]
            except KeyError:
                copies[card_number] = next_cards

            # Initialize cards counter
            try:
                cards[card_number]
            except KeyError:
                cards[card_number] = 1

    return copies


def get_scratchcards(card_copies: list) -> None:
    """Update the cards dictionary recursively.

    :param list card_copies: list of scratchcards to iterate on
    """
    for card in card_copies:
        cards[card] += 1
        if copies[card]:
            get_scratchcards(copies[card])


if __name__ == "__main__":
    with open("2023/day_4/input.txt", "r") as file:
        strings = file.read().split("\n")
        cards = {}
        pattern = r"Card\s+(\d+):(?:\s+)((?:\d+\s*)+)\s\|(?:\s+)((?:\d+\s*)+)"
        copies = get_copies(pattern)
        for card_number, card_copies in copies.items():
            get_scratchcards(card_copies)
        print(f"Total number of scratchcards: {sum(cards.values())}")
