# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head.next):
            return head
        
        temp_head = ListNode(-50001, head)
        hole = head
        head = temp_head
        
        while(hole.next):
            
            if(hole.val <= hole.next.val):
                hole = hole.next
                continue

            temp = head
            while(temp.next.val < hole.next.val):
                temp = temp.next

            nxt = hole.next.next
            hole.next.next = None

            hole.next.next = temp.next
            temp.next = hole.next
            hole.next = nxt

        return head.next
                
                
            
            
            
            
            
            