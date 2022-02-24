# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        
        fast = head
        slow = head
        temp = None
        while(fast and fast.next):
            temp = slow
            slow = slow.next
            fast = fast.next.next

        temp.next = None

        head = self.sortList(head)
        slow = self.sortList(slow)
        return self.mergeList(head, slow)

    def mergeList(self, p1, p2):
        curr = ListNode()
        head = curr
        while(p1 or p2):
            if(not p2 or (p1 and p1.val <= p2.val)):
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next

            curr = curr.next
        return head.next
