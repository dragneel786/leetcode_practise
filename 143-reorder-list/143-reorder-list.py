# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reOrder(head, node):
            if(not head.next):
                head.next = node.next
                node.next = head
                return head.next
            
            node = reOrder(head.next, node)
            if(not node):
                return None
            
            if(node == head or node.next == head):
                head.next = None
                return None
        
            head.next = node.next
            node.next = head
            return head.next
    
        if(head.next and head.next.next):
            reOrder(head, head)
            
            