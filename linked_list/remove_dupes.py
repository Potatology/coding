class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return None
        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else: 
                current = current.next
        return head        







# head = ListNode(6) 
# head.next = ListNode(1)  
# head.next.next = ListNode(6)    
# head.next.next.next = ListNode(6)    
# head.next.next.next.next = ListNode(4) 