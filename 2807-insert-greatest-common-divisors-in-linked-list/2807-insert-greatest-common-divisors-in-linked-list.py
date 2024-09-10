# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(a, b):
            if b == 0:
                return a
            
            return gcd(b, a % b)
        
        
        prev = head
        curr = head.next
        while(prev.next is not None):
            prev.next = ListNode(gcd(prev.val, curr.val), curr)
            prev = curr
            curr = prev.next
        
        return head