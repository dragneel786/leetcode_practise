# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        temp = head
        while(temp):
            n += 1
            temp = temp.next
        
        n = n - 1
        temp = head
        ans = 0
        while(temp):
            ans += (2 ** n * temp.val)
            temp = temp.next
            n -= 1
        
        return ans