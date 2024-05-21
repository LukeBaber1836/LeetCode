# Notion Note: 
# https://www.notion.so/LeetCode-Notes-Python3-f492fbd8c0c140a0a2bdcdbc4342df22?pvs=4

"""
To find if the binary tree is balanced we will be doing a DFS on the tree
If the tree is Null or None, then it is balanced and we can return true
At each node, we will check if the tree is balanced by finding the absolute difference between the heights in the node
If the difference is greater than 1 then the node is unbalanced.
This process will continue until the root node is checked, at which if the difference is still greater than 1,
then the whole tree is unbalanced.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balanced(node):
            if not node: # Base case
                return [True, 0] # Return true since null tree is balanced
            
            # Perform DFS search
            left = balanced(node.left)
            right = balanced(node.right)

            # Find balance of node
            # left and right are True(not null) and
            # left and right height difference is not greater than 1
            balance = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)

            # returns balanced boolean, and height
            return [balance, 1 + max(left[1], right[1])]
        
        return balanced(root)[0] # Index 0 contains the boolean