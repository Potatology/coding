class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        c1 = l1
        c2 = l2
        headRoot = ListNode(-1)
        head = headRoot
        while c1 or c2:
            if not c1:
                head.next = ListNode(c2.val)
                c2 = c2.next
            elif not c2:
                head.next = ListNode(c1.val)
                c1 = c1.next
            else: 
                head.next = ListNode(min(c1.val, c2.val))
                if head.next.val == c1.val:
                    c1 = c1.next
                else: c2 = c2.next
            head = head.next    
        return headRoot.next

        def mergeTwoLists2(self, l1, l2):
            dummy = ListNode(-1)
            head = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else: 
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            if not l1:
                dummy.next = l2
            if not l2:
                dummy.next = l1
        return head.next                