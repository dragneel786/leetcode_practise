# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ahead = head
        for _ in range(n):
            ahead = ahead.next
        
        prev = None
        bhead = head
        while(ahead):
            ahead = ahead.next
            prev = bhead
            bhead = bhead.next
        
        nxt = bhead.next
        if(not prev): return nxt
        prev.next = nxt
        return head