# Notion Note: 
# https://www.notion.so/LeetCode-Notes-Python3-f492fbd8c0c140a0a2bdcdbc4342df22?pvs=4

"""
For this problem, we will use a hashmap to store the elements according to each value
in a list.  Using a min heap, the dictionary elements will be added so that the most
frequent will be on the top of the heap (greatest neg value). Next, for k number of 
elements, we will pop off the heap the elements on top, which will give us the most 
frequent numbers that appear in the array.
"""
from collections import defaultdict
import heapq

# Time complexity O(n log(k)):
# n log(k) comes from min heap
# n size of array and k is size of hash map

# Space complexity is O(n) where n is the size of the hashMap
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Hashmap to store frequency of values in
        hashMap = defaultdict(int)
        
        # Insert into hashMap using number as key
        for num in nums:
            hashMap[num] = hashMap[num] + 1 # Use num as the key

        # Use a min heap to place number from most frequent to least in descending order
        min_heap = []
        for num, frequency in hashMap.items():
            heapq.heappush(min_heap, (-frequency, num)) # use - sinc its a min heap, pushes it to the back
        
        # Pop k number of elements from the heap to find
        top_k_elements = []
        for num in range(k):
            # heapq.heappop(top_k_elements)[1] is the number with highest occurances
            # each time an element is popped the heaps max occurance moved to the next number
            max_occur_num = heapq.heappop(min_heap)[1]
            top_k_elements.append(max_occur_num)
        
        # k most frequen elements
        return top_k_elements





if __name__ == "__main__":
    # Should return "[3,1]" or "[1,3]"
    print(Solution.topKFrequent(1,[5,1,1,1,2,2,3,3,3,3], 2))