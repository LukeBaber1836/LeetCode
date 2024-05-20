# Notion Note: 
# https://www.notion.so/LeetCode-Notes-Python3-f492fbd8c0c140a0a2bdcdbc4342df22?pvs=4

"""
Inverting a binary tree is done with a Post Order Traversal.
We first go left then right, then parent.
Once at parent we switch left tree with right tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # Base case
            return 0

        self.invertTree(root.left) # Calls left subtree
        self.invertTree(root.right) # Calls right subtree

        # Swap the nodes
        root.left, root.right = root.right, root.left
        return root