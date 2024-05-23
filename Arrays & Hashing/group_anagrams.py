# Notion Note: 
# https://www.notion.so/LeetCode-Notes-Python3-f492fbd8c0c140a0a2bdcdbc4342df22?pvs=4

"""
Similar to the previous anagram solution, we will use sorted() to determine if a word is
an anagram.  Start by creating a dictionary of lists with defaltdict(list). Loop through
the array of words and sort the current iteration and use that as a key value for the dictionary.
Using that key value, append the current word into that bucket of the dictionary.  Doing this
will create "groupings" of the anagrams.  Lastly, return the dictionary as a list of lists using
the list() function.
"""

from collections import defaultdict 
# Defaultdict is same as a dict, but it does not raise key error an uses a default
# value if no key is present

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            # sorted word will be the unique key and if word is anagram, sorted will be the same
            sorted_word = ''.join(sorted(word))

            # using sorted_word as the key, append word into that bucket, this will group the anagrams
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values()) # Convert dict to list for correct return type


if __name__ == "__main__":
    # Tests for brute force method
    print(Solution.groupAnagrams(1,["eat","tea","tan","ate","nat","bat"]))