# Notion Note: 
# https://www.notion.so/LeetCode-Notes-Python3-f492fbd8c0c140a0a2bdcdbc4342df22?pvs=4

"""
NOTE: Must run in at least O(n)
Approach: 
 - First handle the empty case scenario
 - Create variables for the largest count and a set of the nums array
 - Loop through each number in nums and check if num - 1 is in the num_set
 - If it is NOT, then this number is the start of a sequence, set a tracker variable
   to num and sequence count to 1
 - While the current_num + 1 is in the num_set (sequence is not finished) increment the
   current num and sequence count by 1
 - Finally, after the while loop, max(longest_sequence, current sequence)
 - After the for loop -> return longest_sequence variable

"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Handles Empty Case
        if len(nums) == 0:
            return 0

        # Variables for tracking
        largest_sequence_count = 0
        num_set = set(nums) # removes duplicates -> O(n)

        for num in nums:

            # Check for start of sequence
            if num - 1 not in num_set:
                current_num = num
                sequence_count = 1

                while current_num + 1 in num_set: # use set to prevent duplicates
                    current_num += 1
                    sequence_count += 1
            
                # Get the longest streak
                largest_sequence_count = max(largest_sequence_count, sequence_count)

        return largest_sequence_count

if __name__ == "__main__":
    # Should return "[24,12,8,6]"
    print(Solution.longestConsecutive(1,[100,4,200,1,3,2]))