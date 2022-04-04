# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        bck = head
        front = head
        for i in range(1, k):
            front = front.next
        
        temp = front
        while(temp.next):
            bck = bck.next
            temp = temp.next
        
        front.val, bck.val = bck.val, front.val
        return head