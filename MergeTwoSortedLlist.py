class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        curr.val = float("-inf")
        head = curr
        while(list1 or list2):
            if((not list2 and list1) or (list1 and list1.val < list2.val)):
                curr.next = list1
                curr = list1
                list1 = list1.next
            
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        return head.next