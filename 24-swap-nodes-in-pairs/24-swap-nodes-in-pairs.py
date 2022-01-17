# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        
        prev = head
        curr = head.next
        head = curr
        temp = None
        while(prev and curr):
            prev.next = curr.next
            curr.next = prev
            if(not temp):
                temp = prev
            else:
                temp.next = curr
                temp = prev
            prev = prev.next
            if(prev):
                curr = prev.next
        
        return head
            