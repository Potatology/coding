class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        valstack = []
        fast, slow = head, head
        while fast and fast.next:
            valstack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        # in case linked list has odd number of nodes
        if fast and not fast.next:
            slow = slow.next
        while slow:
            if valstack.peek() == slow.val:
                valstack.pop()
                slow = slow.next
            else:
                return False
        return valstack.isEmpty()
        