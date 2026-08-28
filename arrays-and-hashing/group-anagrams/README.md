# Anagram Dictionary Groups

## Framing Tier

**Priority 1 — Real System.**

This is the core indexing technique behind anagram/word-game helper tools —
the kind of engine that powers Scrabble and Words With Friends "cheat" or
"assist" apps, as well as standalone anagram-solver and crossword-helper
sites. These tools preprocess a dictionary once: every word is reduced to a
canonical signature (its letters sorted, or a letter-frequency count), and a
hashmap is built from `signature -> [words with that signature]`. At query
time, a player's rack of tiles is reduced to the same kind of signature and
looked up in that map, giving an instant list of every valid word (or
sub-word) they could play. The "group anagrams together" step you're solving
here is exactly that one-time indexing pass — it's the same
canonical-key-into-hashmap technique used to build those word-game
dictionaries.

## Scenario

You're building the indexing layer for a word-game helper app. On startup,
the app loads a batch of words (pulled from a dictionary word list or a
player's recent word history) and needs to group every word together with
all the other words that are anagrams of it — i.e., made of exactly the same
letters, just rearranged. Later, when a player types a word, the app can
instantly show them every other valid word that uses the same tiles by
looking up that word's group.

## Problem Statement

Given a list of words `words`, group the anagrams together so each group
contains only words that are letter-for-letter rearrangements of one
another. Return the groups in any order (and the words within each group in
any order).

## Examples

**Example 1:**
```
Input:  words = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```
Explanation:
- No other word in the list can be rearranged to form `"bat"`.
- `"nat"` and `"tan"` are anagrams — same letters, rearranged.
- `"ate"`, `"eat"`, and `"tea"` are anagrams of each other.

**Example 2:**
```
Input:  words = [""]
Output: [[""]]
```

**Example 3:**
```
Input:  words = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= words.length <= 10^4`
- `0 <= words[i].length <= 100`
- `words[i]` consists of lowercase English letters.

## Diagram

```
Incoming word batch:
  "eat"  "tea"  "tan"  "ate"  "nat"  "bat"

Reduce each word to a canonical signature, then bucket by signature:

  signature("eat") = signature("tea") = signature("ate") = "aet"
  signature("tan") = signature("nat")                     = "ant"
  signature("bat")                                         = "abt"

  "aet" -> ["eat", "tea", "ate"]
  "ant" -> ["tan", "nat"]
  "abt" -> ["bat"]

Output groups = the buckets' values.
```

## Follow-up

No follow-up was included in the original problem statement, so there's
nothing to reframe here.