# Notion Note: 
# https://www.notion.so/LeetCode-Notes-Python3-f492fbd8c0c140a0a2bdcdbc4342df22?pvs=4

"""
To find the max depth of a binary tree we will do a depth first search
By adding 1 to each valid "level" of the tree, and stopping at leafs that have null children,
we can find the max depth by adding up the levels and finding the max
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: # Base case
            return 0

        # root is not null, therefore add 1
        # Depth First Search
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Find greatest depth and return
        return 1 + max(left_depth, right_depth)
    
    #  Time commplexity same ^
    # def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     level = 0
    #     q = deque([root])
        
    #     while q:
    #         for i in range(len(q)):
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
            
    #         level += 1

    #     return level