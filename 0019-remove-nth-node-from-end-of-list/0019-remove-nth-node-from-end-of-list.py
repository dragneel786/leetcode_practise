# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode],\
                         n: int) -> Optional[ListNode]:
        size = 0
        node = head
        while(node):
            node = node.next
            size += 1
        
        temp_head = ListNode(-1, head)
        prev = temp_head
        node = head
        for _ in range(size - n):
            prev = node
            node = node.next
        
        prev.next = node.next
        return temp_head.next
                
        
        
        
            
            
        
        