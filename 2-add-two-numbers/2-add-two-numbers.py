# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp = None
        rem = 0
        while(l1 and l2):
            sumed = l1.val + l2.val + rem
            rem = sumed // 10
            sumed %= 10
            if(not head):
                head = ListNode(sumed)
                temp = head
            else:
                temp.next = ListNode(sumed)
                temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while(l1):
            sumed = l1.val + rem
            rem = sumed // 10
            sumed %= 10
            temp.next = ListNode(sumed)
            temp = temp.next
            l1 = l1.next
            
        while(l2):
            sumed = l2.val + rem
            rem = sumed // 10
            sumed %= 10
            temp.next = ListNode(sumed)
            temp = temp.next
            l2 = l2.next
            
        if(rem > 0):
            temp.next = ListNode(rem)
        
        return head