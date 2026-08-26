from typing import List


def find_matching_cards(balances: List[int], price: int) -> List[int]:
    """
    Given a list of gift card balances and a target price, return the
    indices of the two cards whose balances sum exactly to the price.

    Args:
        balances: List of gift card balances.
        price: The exact price to match using two cards.

    Returns:
        A list of two indices into `balances`.
    """
    # your code here
    seen_gift_card_balances = {}

    for i in range(len(balances)):
        diff = price - balances[i]

        if diff in seen_gift_card_balances:
            return [seen_gift_card_balances[diff], i]
        seen_gift_card_balances[balances[i]] = i

    # Time Complexity: O(balances)
    # Space Complexity: O(balances)


if __name__ == "__main__":
    print(find_matching_cards([2, 7, 11, 15], 9))  # expected: [0, 1]
    print(find_matching_cards([3, 2, 4], 6))        # expected: [1, 2]
    print(find_matching_cards([3, 3], 6))           # expected: [0, 1]