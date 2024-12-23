# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        def swap_count(values):
            c = 0
            idx_map = {v: i for i, v in enumerate(values)}
            vals = sorted(values)
            for i in range(len(values)):
                if values[i] != vals[i]:
                    values[i], values[idx_map[vals[i]]] =\
                    values[idx_map[vals[i]]], values[i]
                    idx_map[values[idx_map[vals[i]]]] = idx_map[values[i]]
                    c += 1
            
            return c    
        
        q = deque([root])
        ans = 0
        while(q):
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    level.append(node.left.val)
                    q.append(node.left)
                
                if node.right:
                    level.append(node.right.val)
                    q.append(node.right)
            
            
            ans += swap_count(level)
        
        return ans
                