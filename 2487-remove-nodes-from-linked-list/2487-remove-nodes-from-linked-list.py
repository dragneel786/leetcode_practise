# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def remove_nodes(head):
            if(not head.next):
                return head

            head.next = remove_nodes(head.next)
            if(head.next and head.next.val > head.val):
                return head.next
            return head
            
        return remove_nodes(head)