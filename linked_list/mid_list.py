class Solution:
    def middleNode(self, head):
        slow, fast = head
        while fast:
            if not fast.next:
                return slow
            else:
                fast = fast.next
                slow = slow.next
            if not fast.next:
                return slow
            else: 
                fast = fast.next
