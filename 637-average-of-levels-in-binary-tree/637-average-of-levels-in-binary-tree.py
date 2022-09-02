# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def dfs(root, level = 0):
            if(not root):
                return 
            
            val, size = sum_count[level]
            sum_count[level] = [val + root.val, size + 1]
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            
            
        sum_count = defaultdict(lambda:[0, 0])
        dfs(root)
        return [val / size for val, size in sum_count.values()]         
                
            
            
        