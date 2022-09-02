# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = deque([root])
        res = []
        
        while(q):
            temp = 0
            size = len(q)
            
            for _ in range(size):
                node = q.popleft()
                temp += node.val
                if(node.left): q.append(node.left)
                if(node.right): q.append(node.right)
            
            res.append(temp / size)
        
        return res
                    
                
            
            
        