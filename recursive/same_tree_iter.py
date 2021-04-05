class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            return p == q
        deq = []
        deq.append(p)
        deq.append(q)
        while deq != []:
            cp = deq.pop(0)
            cq = deq.pop(0)
            if cp.val != cq.val:
                return False
            if cp.left or cq.left:
                if cp.left and cq.left:
                    deq.append(cp.left)
                    deq.append(cq.left)
                if (not cp.left and cq.left) or (cp.left and not cq.left):
                    return False
            if cp.right or cq.right:
                if cp.right and cq.right:
                    deq.append(cp.right)
                    deq.append(cq.right)
                if (not cp.right and cq.right) or (cp.right and not cq.right):
                    return False
        return True

                        
                    

                    