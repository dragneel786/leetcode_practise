# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def remove_nodes(head):
            nonlocal max_val
            if(not head):
                return None

            head.next = remove_nodes(head.next)
            if(max_val > head.val):
                return head.next
            
            max_val = head.val
            return head
            
            
        
        max_val = -inf
        return remove_nodes(head)