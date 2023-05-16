# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not head or not head.next):
            return head
        
        prev = ListNode()
        thead = head
        head = prev
        
        while(thead and thead.next):
            prev.next = thead.next
            prev = prev.next
            thead.next = prev.next
            prev.next = thead
            thead = thead.next
            prev = prev.next
            
            
        return head.next
            
            
            