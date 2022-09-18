# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        temp = new_head
        
        while(list1 or list2):
            if(not list1 or (list2 and list2.val < list1.val)): 
                temp.next = list2
                list2 = list2.next
            
            else:
                temp.next = list1
                list1 = list1.next
        
            if(temp.next): temp = temp.next
        
        return new_head.next