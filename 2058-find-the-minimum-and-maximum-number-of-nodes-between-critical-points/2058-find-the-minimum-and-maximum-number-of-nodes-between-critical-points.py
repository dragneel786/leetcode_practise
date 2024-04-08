# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minima_idx = []
        prev = head
        curr = head.next
        nxt = curr.next
        idx = 2
        while(nxt):
            if(prev.val > curr.val < nxt.val):
                minima_idx.append(idx)
            
            elif(prev.val < curr.val > nxt.val):
                minima_idx.append(idx)
            
            idx += 1
            prev, curr, nxt = curr, nxt, nxt.next
        
        if(len(minima_idx) < 2):
            return [-1, -1]
        
        min_val = inf
        for i in range(1, len(minima_idx)):
            min_val = min(min_val, minima_idx[i] - minima_idx[i - 1])
        
        return [min_val, minima_idx[-1] - minima_idx[0]]