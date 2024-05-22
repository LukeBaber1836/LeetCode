"""
Brute Force:
There are multiple ways to solve this problem, an iterative way would be to
loop through the array while keeping a list of seen values.  If any of the values appear
again in the seen list then a duplicate has been found.

Hashtable:
The way it is solved below is by using a set().  A set cannot have duplicates,
therefore if the nums array is converted to a set, and the length has decreased
by any amount, then the nums array contained duplicates.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Convert nums to set, if set len is shorter than len of nums
        # Then a duplicate was in the nums array
        if (len(set(nums)) < len(nums)):
            return True
        else:
            return False