"""
Brute Force:
Loop through the array and check every single value in the array with the current
element to see if the sum adds up to the target number.  Continue until all elements have
been tested.  If no two sum indices are found, return an empty array.

Optimized:
Use a hashmap to keep track of numbers and their indices. For each number in the array, subtract it from
the target number.  This will create a complement, and if that complement is present in the hashmap
then we have an answer.  If the complement is in the Hashmap and the complement's index is not the current
index of the for loop (repeat element), then return the index and the index of the complement stored in the hashmap.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []

        # O(n^2) time -> Brute force not time efficient
        # O(n) space -> N is length of result array
        for index,number in enumerate(nums):
            for test_index, test_num in enumerate(nums):
                if (test_index != index) and (number + test_num == target):
                    result = [index, test_index]
                    break
        return result
    
    def twoSum_2(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        
        # O(n) time
        # O(n) space -> N is size of hashMap
        for i in range(len(nums)):
            complement = target - nums[i] # Subtracting the current num from target, search for result in hashMap

            # complement in hashMap, and its index is not the same as i
            if (complement in hashMap) and (hashMap[complement] != i):
                return [i, hashMap[complement]]
            
            hashMap[nums[i]] = i # Add 


if __name__ == "__main__":
    # # Tests for brute force method
    # print(Solution.twoSum(1,[2,7,11,15],9))
    # print(Solution.twoSum(1,[3,2,4],6))
    # print(Solution.twoSum(1,[3,3],6))
    # print(Solution.twoSum(1,[3,3],7))

    # Tests for optimized method
    print(Solution.twoSum_2(1,[2,7,11,15],9))
    print(Solution.twoSum_2(1,[3,2,4],6))
    print(Solution.twoSum_2(1,[3,3],6))
    print(Solution.twoSum_2(1,[3,3],7))