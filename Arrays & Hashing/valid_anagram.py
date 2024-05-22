"""
Sorted is the easiest way, but not the most efficient as it is O(n log(n))

For this problem, I performed a for loop over each element in the
given string. First, make sure both strings are the same length.  
Next, using Python's "in" method, I can check if the current
element in the for loop appears in the other string as well.  If it does
not, then it is not a valid anagram.
"""

class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        # Sort t and s, if they are the same, then it is an anagram
        # Time complexity O(n log(n)), 
        # sorted() has n log(n) time complexity on average
        return sorted(t) == sorted(s)

        # Alternate way
        # Check different lengths
        if len(s) != len(t):
            return False
            
            
    def isAnagram2(self, s: str, t: str) -> bool:
        # Dictionary to store the count of each element
        hashMap = {}
        #Check letters in s, add up occurrences
        for x in s:
            hashMap[x] = hashMap.get(x, 0) + 1 # counts letter
        
        #Check letters in t, subtract occurrences
        for y in t:
            if y not in hashMap or hashMap[y] == 0: # Letter doesn't occur or there are too few
                return False
            else: hashMap[y] -= 1
        
        return True


if __name__ == "__main__":
    # Tests for method 1
    print(Solution.isAnagram1("null", "aacc","cca"))
    print(Solution.isAnagram1("null", "anagram","nagaram"))
    print(Solution.isAnagram1("null", "rat","car"))
    print(Solution.isAnagram1("null", "aacc","ccac"))

    # Tests for method 2
    print(Solution.isAnagram2("null", "aacc","cca"))
    print(Solution.isAnagram2("null", "anagram","nagaram"))
    print(Solution.isAnagram2("null", "rat","car"))
    print(Solution.isAnagram2("null", "aacc","ccac"))