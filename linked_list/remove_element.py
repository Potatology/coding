class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        newHead = ListNode(-1)
        newHead.next = head
        current = newHead
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return newHead.next

# head = ListNode(6) 
# head.next = ListNode(1)  
# head.next.next = ListNode(6)    
# head.next.next.next = ListNode(6)    
# head.next.next.next.next = ListNode(4) 

outputNode = Solution().removeElements(head, 6)

out = outputNode
while out:
    print(out.val)
    out = out.next