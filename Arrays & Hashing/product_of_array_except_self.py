# Notion Note: 
# https://www.notion.so/LeetCode-Notes-Python3-f492fbd8c0c140a0a2bdcdbc4342df22?pvs=4

"""
For this question we will create an array of 1s that is the length of nums.

Going from 0 to n (length of nums) -> left to right
Using a for loop, find the left product of the array by first assigning the left
product to the current index of the result array, and then updating the left product
by multiplying itsselft by the current index of the nums array.

Going from n (length of nums) to 0 (including 0) -> right to left
Using another for loop, find the right product of the array by multiplying the
current index of the result, by the right product.  Next update the right product
variable by multiplying it by itself and the current index of nums

This algorithim will for the prefix and suffix products of the array without
multiplying an ellement by itself.
"""

# Time complexity is O(2n) which reduces down to O(n):
# Space complexity is O(n) -> n is the length of nums

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Initialize array of 1s that is the length of nums
        result = [1] * len(nums)

        # Calculate left products and store in result
        left_product = 1
        for i in range(len(nums)):
            result[i] = left_product
            left_product = left_product * nums[i] # update for next iteration
        
        # Calculate right products and multiply with the left product results array
        # Go from right to left, and stop at -1
        # range(start=len(nums) - 1, stop=-1, step=-1)
        right_product = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] = result[j] * right_product
            right_product = right_product * nums[j]
        
        return(result)




if __name__ == "__main__":
    # Should return "[24,12,8,6]"
    print(Solution.productExceptSelf(1,[1,2,3,4]))