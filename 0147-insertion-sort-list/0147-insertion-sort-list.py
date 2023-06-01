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
        hole = head.next
        prev_hole = head
        head = temp_head
        
        while(hole):
            if(prev_hole.val <= hole.val):
                prev_hole = hole
                hole = hole.next
                continue
            
            prev_hole.next = hole.next
                
            temp = head
            while(temp.next.val < hole.val):
                temp = temp.next
            
            hole.next = temp.next
            temp.next = hole
            
            hole = prev_hole.next

        return head.next
                
                
            
            
            
            
            
            