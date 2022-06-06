# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1 = headA
        n2 = headB
        while(n1 != n2):
            n1 = headB if not n1 else n1.next
            n2 = headA if not n2 else n2.next
        return n1