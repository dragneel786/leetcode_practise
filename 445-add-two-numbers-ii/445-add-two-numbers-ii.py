# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = deque()
        st2 = deque()
        while(l1):
            st1.append(l1.val)
            l1 = l1.next
        
        while(l2):
            st2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None
        while(len(st1) or len(st2) or carry):
            val1 = 0
            val2 = 0
            if(len(st1)):
                val1 = st1.pop()
            if(len(st2)):
                val2 = st2.pop()
            
            ans = val1 + val2 + carry
            carry = ans // 10
            temp = ListNode(ans % 10, head)
            head = temp
        
        return head
            
        
        
        