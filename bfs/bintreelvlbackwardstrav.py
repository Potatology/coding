class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        if not root.left and not root.right:
            return [[root.val]]
        q = []
        res = []
        q.append(root)
        while q != []:
            size = len(q)
            lvl = []
            while size > 0:
                cn = q.pop(0)
                if cn.left:
                    q.append(cn.left)
                if cn.right:
                    q.append(cn.right)
                lvl.append(cn.val)
                size -= 1
            res.append(lvl)
        return res[::-1]