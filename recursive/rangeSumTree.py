class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def helper(self, node, low, high):
            if not node:
                return 0
            if node.val in range(low, high + 1):
                return node.val + helper(self, node.left, low, high) + helper(self, node.right, low, high)
            else:
                return helper(self, node.left, low, high) + helper(self, node.right, low, high)
        return helper(self, root, low, high)
    