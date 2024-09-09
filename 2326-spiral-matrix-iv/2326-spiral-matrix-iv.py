# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        res = [([-1] * n) for _ in range(m)]
        right, left = 0, n
        top, bottom = 0, m
        while(head is not None):
            # Right
            for j in range(right, left):
                if head is None:
                    return res
                
                res[top][j] = head.val
                head = head.next
            top += 1
            
            # Bottom
            for j in range(top, bottom):
                if head is None:
                    return res
                
                res[j][left - 1] = head.val
                head = head.next
            left -= 1
            
            # Left
            for j in range(left - 1, right - 1, -1):
                if head is None:
                    return res
                
                res[bottom - 1][j] = head.val
                head = head.next
            bottom -= 1
            
            # Top
            for j in range(bottom - 1, top - 1, -1):
                if head is None:
                    return res
                
                res[j][right] = head.val
                head = head.next
            right += 1
        
        return res
        