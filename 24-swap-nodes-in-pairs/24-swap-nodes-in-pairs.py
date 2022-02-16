# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        
        prev = head
        curr = head.next
        head = ListNode(0, head)
        next = head
        while(True):
            next.next = curr
            prev.next = curr.next
            curr.next = prev
            next = prev
            if(not next.next or not next.next.next):
                return head.next
            prev = next.next
            curr = prev.next
            
        
                
            