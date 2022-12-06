# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not head):
            return head
        
        h1 = head
        second = h2 = head.next
        
        while(h2 and h2.next):
            h1.next = h2.next
            h2.next = h2.next.next
            
            h1 = h1.next
            h2 = h2.next
        
        h1.next = second
        return head
            
        