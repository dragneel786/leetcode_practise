# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         fast = slow = head
#         while(fast.next and fast != slow):
#             fast = fast.next.next
#             slow = slow.next
        
#         print(fast.val, slow.val)
        hmap = dict()
        node = head
        while(node and node not in hmap):
            hmap[node] = 1
            node = node.next
        
        return node