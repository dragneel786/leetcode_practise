# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(not head or not head.next):
            return False
        
        if(head.next == head):
            return True
        
        slow = head
        fast = head
        while(True):
            slow = slow.next
            fast = fast.next.next
            if(not fast or not fast.next):
                return False
            if(fast == slow):
                return True