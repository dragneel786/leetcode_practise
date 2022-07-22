# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        newHead = ListNode()
        nh = newHead
        temp = head
        prev = None
        while(temp):
            if(temp.val < x):
                nh.next = temp
                nh = temp
                if(not prev):
                    head = head.next
                    temp = head
                else:
                    prev.next = temp.next
                    temp = prev.next
            else:
                prev = temp
                temp = temp.next
        
        nh.next = head
        return newHead.next
                    
                    
                    
                    
        
        