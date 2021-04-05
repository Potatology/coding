# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = []
        queue.append(root)
        while queue != []:
            levelSize = len(queue)
            level = []
            while levelSize > 0:
                curNode = queue.pop(0)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                level.append(curNode.val)
                levelSize -= 1
            result.append(level)
        return result
        