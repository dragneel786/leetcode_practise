# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return None
        
        fast = head.next.next
        slow = head.next
        while(fast and fast.next and fast != slow):
            fast = fast.next.next
            slow = slow.next
        
        slow = head
        while(fast and fast.next and fast != slow):
            fast = fast.next
            slow = slow.next
        
        return slow if(fast and fast.next) else None