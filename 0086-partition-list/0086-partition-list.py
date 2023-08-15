# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        t1 = h1 = ListNode(0)
        t2 = h2 = ListNode(0)
        while(head):
            nxt = head.next
            head.next = None
            if(head.val < x):
                t1.next = head
                t1 = t1.next
            else:
                t2.next = head
                t2 = t2.next
            
            head = nxt
            
        t1.next = h2.next
        return h1.next