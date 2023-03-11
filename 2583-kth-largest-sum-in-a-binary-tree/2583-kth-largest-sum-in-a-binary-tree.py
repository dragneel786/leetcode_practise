# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        def sum_it(node):
            q = deque([node])
            while(q):
                level_sum = 0
                for _ in range(len(q)):
                    poped = q.popleft()
                    if(not poped):
                        continue
                    
                    level_sum += poped.val
                    q.append(poped.left)
                    q.append(poped.right)
                
                sums.append(level_sum)
                
        sums = []
        sum_it(root)
        return nlargest(k, sums)[-1] if(len(sums) - 1 >= k) else -1