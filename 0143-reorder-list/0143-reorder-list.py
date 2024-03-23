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
        deq = deque()
        while(head):
            deq.append(head)
            head = head.next
            
        new_head = temp = ListNode(-1)
        while(deq):
            node1, node2 = deq.popleft(), None
            if(deq):
                node2 = deq.pop()
            
            temp.next = node1
            node1.next = node2
            temp = node2
            if(temp):
                temp.next = None
            
        
        head = new_head.next
            
        
        
        