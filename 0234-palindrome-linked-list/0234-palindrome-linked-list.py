# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        deq = deque()
        while(head):
            deq.append(head)
            head = head.next
        
        while(deq):
            if(len(deq) == 1):
                break
            
            node1, node2 = deq.popleft(), deq.pop()
            if(node1.val != node2.val):
                return False
        
        return True
            
            
            
            
            
            