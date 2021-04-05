# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: 
            return 0
        return (mdSide(root, 0))
    def mdSide(n: TreeNode, cd: int) -> int:
            if not n:
                return cd
            return max(mdSide(n.left, cd + 1), mdSide(n.right, cd + 1))
        
        
