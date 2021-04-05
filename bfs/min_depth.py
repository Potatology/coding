# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        q = []
        q.append(root)
        md = 1
        while q != []:
            s = len(q)
            while s > 0:
                cn = q.pop(0)
                if not cn.left and not cn.right:
                    return md
                if cn.left:
                    q.append(cn.left)
                if cn.right:
                    q.append(cn.right)
                s -= 1
            md += 1
        return md