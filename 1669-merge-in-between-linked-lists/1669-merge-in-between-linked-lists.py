# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = None
        curr = list1
        idx = 0
        while(idx < a):
            prev = curr
            curr = curr.next
            idx += 1
    
        while(idx < b):
            curr = curr.next
            idx += 1
        
        curr = curr.next
        
        new_curr = list2
        while(new_curr.next != None):
            new_curr = new_curr.next
        
        prev.next = list2
        new_curr.next = curr
        return list1
            
            
        