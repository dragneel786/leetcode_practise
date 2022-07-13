# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        def levelInDFS(root, l):
            if(not root):
                return
            
            if(l == len(res)):
                res.append([])
                
            res[l].append(root.val)
            levelInDFS(root.left, l + 1)
            levelInDFS(root.right, l + 1)
            
        
        res = []
        levelInDFS(root, 0)
        return res