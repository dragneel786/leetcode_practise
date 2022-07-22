# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode()
        after_head = ListNode()
        bh, ah = before_head, after_head
        temp = head
        while(temp):
            if(temp.val < x):
                bh.next = temp
                bh = temp
            else:
                ah.next = temp
                ah = temp
            temp = temp.next
        
        ah.next = None
        bh.next = after_head.next
        return before_head.next
                    
                    
                    
        
        