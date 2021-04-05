class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseLinkedList(head):
    rev = None
    cur = head
    while cur:
        rev, rev.next, cur = cur, rev, cur.next
    print(f'{rev.val}, {rev.next.val}, {rev.next.next.val},{rev.next.next.next.val},{rev.next.next.next.next.val}')
    return rev

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)    
head.next.next.next = ListNode(4)    
head.next.next.next.next = ListNode(5)

print(reverseLinkedList(head))
