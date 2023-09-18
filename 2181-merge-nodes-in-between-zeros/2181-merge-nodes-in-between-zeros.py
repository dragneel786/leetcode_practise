# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = new_head = ListNode(-1)
        val = 0
        head = head.next
        while(head):
            val += head.val
            if(not head.val):
                new_node = ListNode(val)
                curr.next = new_node
                val = 0
                curr = new_node
                
            head = head.next
        
        return new_head.next
            