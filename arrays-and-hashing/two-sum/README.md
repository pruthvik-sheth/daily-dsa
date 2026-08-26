# Gift Card Balance Matcher

## Scenario

A customer at checkout has a wallet full of gift cards, each with its own
balance. They want to pay for an item using **exactly two** gift cards
whose balances add up to the item's price, with no leftover balance and
no top-up needed. You're building the checkout logic that figures out
which two cards to apply.

## Problem Statement

Given an array of integers `balances`, where `balances[i]` is the balance
on the `i`-th gift card in the wallet, and an integer `price`, return the
indices of the two gift cards whose balances add up exactly to `price`.

You may assume each wallet has exactly one valid pair of cards that
works, and you cannot use the same card twice. Return the two indices in
any order.

## Examples

**Example 1:**
```
Input: balances = [2,7,11,15], price = 9
Output: [0,1]
Explanation: balances[0] + balances[1] == 9, so cards 0 and 1 are used.
```

**Example 2:**
```
Input: balances = [3,2,4], price = 6
Output: [1,2]
```

**Example 3:**
```
Input: balances = [3,3], price = 6
Output: [0,1]
```

## Constraints

- `2 <= balances.length <= 10^4`
- `-10^9 <= balances[i] <= 10^9`
- `-10^9 <= price <= 10^9`
- Only one valid pair of cards exists.

## Follow-up

Can you design the checkout matcher so it runs in less than `O(n^2)` time,
i.e. without checking every possible pair of cards one by one?