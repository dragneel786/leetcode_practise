# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(not head or not head.next or not k):
            return head
        n = 1
        temp = head
        while temp:= temp.next:
            n += 1
        
        k = n - k % n
        if(not k or k == n):
            return head
        
        prev = head
        curr = head.next
        while k:= k - 1:
            prev = curr
            curr = curr.next
        
        prev.next = None
        temp = curr
        while(curr.next):
            curr = curr.next
        
        curr.next = head
        head = temp
        return head
                
        
        
            