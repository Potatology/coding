# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root.left == None and root.right == None:
            if root.val = 0:
                return 0
        queue = []
        avgs = []
        queue.append(root)
        while queue != []:
            queuesize = len(q)
            denominator = queuesize
            numerator = 0
            while queuesize > 0:
                current = queue.pop(0)
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
                numerator += current.val
                queuesize -= 1
            avgs.append(numerator/denominator)
        return avgs
