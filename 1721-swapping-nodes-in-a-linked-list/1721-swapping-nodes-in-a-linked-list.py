# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p1 = last = head
        for _ in range(1, k):
            p1 = p1.next
            last = last.next
        
        p2 = head
        while(last.next):
            p2 = p2.next
            last = last.next
        
        p1.val, p2.val = p2.val, p1.val
        return head
        