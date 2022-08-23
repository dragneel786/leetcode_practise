# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def check(fast, slow):
            if(not fast or not fast.next):
                node = slow if(not fast) else slow.next
                return True, node
            
            ret, node = check(fast.next.next, slow.next)
            return (ret and node.val == slow.val), node.next
        
        
        return check(head, head)[0]
                      