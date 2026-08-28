from typing import List
from collections import defaultdict

def groupAnagrams_bruteforce(strs: List[str]) -> List[List[str]]:
    def are_anagrams(s, t):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    groups : List[List[str]] = []

    for word in strs:
        placed = False
        for group in groups:
            if are_anagrams(word, group[0]):
                group.append(word)
                placed = True
                break
        if not placed:
            groups.append([word])

    return groups

def groupAnagrams_sorting(strs):
    # For each and every incoming word we sort it
    # After the word is sorted we treat that word as
    # a key for our hashmap and add the unsorted version
    # of the word in our group

    map = defaultdict(list) # Initialize the hash map and value to be an empty array

    for word in strs:
        sorted_word = ''.join(sorted(word))
        map[sorted_word].append(word)

    return list(map.values())


# Hast table solution
def groupAnagrams_hash_table(strs):
    # Approach
    # Create a hash map where:
        # Each key: is a length 26 tuple representing char freqs
        # Each Value: Is a list of strings belonging to that group
    
    # For each string in the input:
        # Intialize a count array of size 26 with all zeros
        # For each char in that string, we incre the count at the corrsponding idx
        # Convert the count array to tuple to use it as a key
        # Append the string to the list associated with that key

    # Finally after processing all the strings, we return
    # all the lists stored in the hash map

    res = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(word)
    return list(res.values())

    # Time Complexity: 
    # m = total strings
    # n = longest string length

