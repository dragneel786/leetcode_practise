# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        node = prev = ListNode(-1, head)
        curr = head
        val_set = set(nums)
        while(curr != None):
            if curr.val in val_set:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = prev.next
                curr = curr.next
        
        return node.next