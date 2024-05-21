# Notion Note: 
# https://www.notion.so/LeetCode-Notes-Python3-f492fbd8c0c140a0a2bdcdbc4342df22?pvs=4

"""
To find the max diameter of a binary tree we will use a Depth First Search (DFS)
After base case start with 1 as the height and recursively add the max height at each node
Both sides will be added up and maxed at the root of the tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def diameter(node, result):
            if not node: # Base case
                return 0
            
            # Recursively search left and right (DFS)
            left = diameter(node.left, result)
            right = diameter(node.right, result)

            # Update to max depth so far
            result[0] = max(result[0], left + right)
            print(result[0])

            # Return the depth of the current node
            return 1 + max(left, right)
        
        # Value to store diameter
        result = [0]
        diameter(root, result) # Function call from root of tree

        return result[0]