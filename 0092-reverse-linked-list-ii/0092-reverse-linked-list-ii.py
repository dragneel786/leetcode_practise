# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        rhead = prev = ListNode(0, head)
        curr = head
        while(count < left):
            prev = curr
            curr = curr.next
            count += 1
        
        new_prev = None
        new_head = curr
        while(count <= right):
            nxt = curr.next
            curr.next = new_prev
            new_prev = curr
            curr = nxt
            count += 1
            
        prev.next = new_prev
        new_head.next = curr
        
        return rhead.next
        
        
        
            
            
            
            
        