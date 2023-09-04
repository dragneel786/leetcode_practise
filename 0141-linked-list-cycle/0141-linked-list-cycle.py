# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nxt = None):
        self.val = x
        self.next = nxt

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while(fast and fast.next):
            if(fast.next.next == slow):
                return True
            fast = fast.next.next
            slow = slow.next
        return False
        
            