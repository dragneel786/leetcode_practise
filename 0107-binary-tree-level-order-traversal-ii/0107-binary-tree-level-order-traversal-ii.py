# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []
        
        def postorder(node, l = 0):
            if(not node):
                return
            
            if(len(levels) == l):
                levels.append([])
                
            levels[l].append(node.val)
            postorder(node.left, l + 1)
            postorder(node.right, l + 1)
        
        postorder(root)
        return levels[::-1]