# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def check_palindrome(left, right):
            if(not right.next):
                return left.next, left.val == right.val
                
            left, is_valid = check_palindrome(left, right.next)
            return left.next, (is_valid and left.val == right.val)
        
        return check_palindrome(head, head)[1]
            