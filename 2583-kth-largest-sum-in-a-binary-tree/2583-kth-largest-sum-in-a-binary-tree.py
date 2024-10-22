# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        q = deque([root])
        heap = []
        while(q):
            curr_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if len(heap) < k or heap[0] < curr_sum:
                heappush(heap, curr_sum)
            
            if len(heap) > k:
                heappop(heap)
        
        return heap[0] if len(heap) == k else -1
                
        