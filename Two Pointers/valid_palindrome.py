# Notion Note: 
# https://www.notion.so/LeetCode-Notes-Python3-f492fbd8c0c140a0a2bdcdbc4342df22?pvs=4

"""
Two Pointer:
Convert string to only alphanumerics and put into lower case.
For loop through the string using a pointer at the front and
one at the back of the string.  With each iteration the pointers
will converge one step at a time, once in the middle, if they have
been the same value for each iteration up to this point, then 
return true as the string is a valid palindrome.

Simple Method:
Convert string to only alphanumerics and put into lower case.
Using the string[::-1] to list the string backwards, compare
and return if the forward string is equal to the backwards one.

"""

class Solution:
    # Two pointers method
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum,s)) # Keep only alpha numeric letters
        s = s.lower() # Convert to lower case

        # Check for empty case -> " "
        if len(s) == 0:
            return True

        for index in range(len(s)):

            # Two "pointers" to track the palindrome and see if it is valid
            left_pointer = s[index]
            right_pointer = s[len(s) - 1 - index]

            if (left_pointer != right_pointer): # If pointers dont match, palindrome is not valid
                return False
            
            if (index >= len(s) - 1 - index): # Pointers have met in the middle
                return True
    
    # Simple method -> [::-1] will invert the string
    def isPalindrome_2(s):
        # Filter out non-alphanumeric characters and convert to lowercase
        s = ''.join(filter(str.isalnum,s)) # Keep only alpha numeric letters
        s = s.lower() # Convert to lower case
        
        # Check if the filtered string is equal to its reverse
        return s == s[::-1]

if __name__ == "__main__":
    # Tests for brute force method
    print(Solution.isPalindrome(1,"A man, a plan, a canal: Panama"))
    # print(Solution.isPalindrome_2("aa"))