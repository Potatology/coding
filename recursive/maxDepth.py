# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        
### this is a slow recursive that returned time limit exceeded in leetcode

    def maxDepth2(self, root: TreeNode) -> int:
        def helper(node: TreeNode, sum: int) -> int:
            if not node:
                return sum
            return max(helper(node.left, sum + 1), helper(node.right, sum + 1))
        return helper(root, 0)