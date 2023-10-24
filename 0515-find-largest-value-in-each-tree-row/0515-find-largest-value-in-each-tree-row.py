# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node, idx):
            if(not node):
                return
            
            if(len(res) <= idx):
                res.append(node.val)
            
            res[idx] = max(node.val, res[idx])
            dfs(node.left, idx + 1)
            dfs(node.right, idx + 1)
        
        res = []
        dfs(root, 0)
        return res
                