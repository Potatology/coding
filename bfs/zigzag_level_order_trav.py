# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        ltr = True
        que = []
        que.append(root)
        while que != []:
            lsize = len(que)
            level = []
            while lsize > 0:
                cn = que.pop(0)
                if cn.left:
                    que.append(cn.left)
                if cn.right:
                    que.append(cn.right)
                level.append(cn.val)
                lsize -= 1 
        if ltr:
            result.append(level)
            ltr = False
        else:
            result.append(level[::-1])
            ltr = True
        return result

        
        