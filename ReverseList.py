class Solution:
    def reverseList(self, head: Optional[ListNode], h = []) -> Optional[ListNode]:
        curr = head
        prev = None
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev