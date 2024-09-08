# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        tot_size = 0
        temp = head
        while(temp != None):
            tot_size += 1
            temp = temp.next
        
        part_size = tot_size // k
        remain = tot_size % k
        temp = head
        res = []
        while(temp != None):
            prev = ListNode(-1, temp)
            res.append(temp)
            for _ in range(part_size + (remain > 0)):
                prev = prev.next
                temp = temp.next
            
            prev.next = None
            remain -= 1
        
        while(len(res) < k):
            res.append(None)
        
        return res
            
        
            