# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(not lists):
            return None
        
        def merger(lists):
            if(len(lists) - 1 >= 1):
                mid = (len(lists) - 1) // 2
                one = merger(lists[0: mid + 1])
                two = merger(lists[mid + 1:])
                # print(one, two)
                return mergeThem([one, two])
            return lists[0]
        
        def mergeThem(lists):
            head = ListNode()
            temp = head
            first = lists[0]
            second = lists[1]
            while(first and second):
                if(first.val < second.val):
                    temp.next = first
                    first = first.next
                else:
                    temp.next = second
                    second = second.next
                temp = temp.next
            
            while(first):
                temp.next = first
                first = first.next
                temp = temp.next
            
            while(second):
                temp.next = second
                second = second.next
                temp = temp.next
            return head.next
        
        return merger(lists)
            