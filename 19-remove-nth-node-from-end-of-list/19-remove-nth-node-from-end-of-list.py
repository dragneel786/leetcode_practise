# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        end_marker = head
        for _ in range(n):
            end_marker = end_marker.next
        
        
        nth_node = head
        before = None
        while(end_marker):
            before = nth_node
            nth_node = nth_node.next
            end_marker = end_marker.next
        
        if(not before):
            head = head.next
        else:
            before.next = nth_node.next
        
        return head
            
            
        