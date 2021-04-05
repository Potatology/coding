# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        fast = head
        slow = head
        if head == None:
            return False
        while slow.next != None and fast.next != None:
            slow = slow.next
            if fast.next.next == None:
                return False
            fast = fast.next.next
            if fast == slow:
                return True
        return False