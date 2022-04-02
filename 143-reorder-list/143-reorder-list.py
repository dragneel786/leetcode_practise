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
        def orderMyList(head, node):
            if(not head):
                return node
            node = orderMyList(head.next, node)
            if(not node):
                return None

            if(node == head or node.next == head):
                head.next = None
                return None

            temp = node.next
            node.next = head
            head.next = temp
            return temp
        
        orderMyList(head, head)