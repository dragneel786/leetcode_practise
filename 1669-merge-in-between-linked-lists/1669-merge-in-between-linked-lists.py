# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail = list2
        while(tail.next):
            tail = tail.next
        
        temp = list1
        prev = None
        idx = 0
        while(temp and idx < a):
            prev = temp
            temp = temp.next
            idx += 1
        
        while(temp and idx < b):
            temp = temp.next
            idx += 1
        
        prev.next = list2
        # print(prev.val, temp)
        tail.next = temp.next
        return list1
        
            
            
            
        