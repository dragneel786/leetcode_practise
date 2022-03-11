# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        
        n = 0
        temp = head
        last = None
        while(temp):
            n += 1
            last = temp
            temp = temp.next
        
        k = n - (k % n) - 1
        temp = head
        while(k):
            temp = temp.next
            k -= 1
        
        last.next = head
        head = temp.next
        temp.next = None
        return head