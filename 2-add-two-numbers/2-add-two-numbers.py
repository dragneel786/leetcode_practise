# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        temp = head
        while(l1 or l2):
            val1 = 0
            val2 = 0
            if(l1):
                val1 = l1.val
                l1 = l1.next
            if(l2):
                val2 = l2.val
                l2 = l2.next
            ans = val1 + val2 + carry
            carry = ans // 10
            temp.next = ListNode(ans % 10)
            temp = temp.next
        
        if(carry):
            temp.next = ListNode(carry)
        
        return head.next
            
        