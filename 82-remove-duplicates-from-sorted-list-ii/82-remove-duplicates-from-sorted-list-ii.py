# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        
        prev = head
        curr = head.next
        head = ListNode(-101)
        newList = head
        count = 1
        while(curr):
            if(prev.val != curr.val):
                if(count == 1):
                    newList.next = prev
                    newList = newList.next
                count = 0
            
            curr = curr.next
            prev = prev.next
            count += 1
        
        if(count == 1):
            newList.next = prev
            newList = newList.next
            
        newList.next = None
        return head.next
            