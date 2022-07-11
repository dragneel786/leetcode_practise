# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def getRightView(root, l):
            if(not root):
                return
            
            levels[l] = root.val
            getRightView(root.left, l + 1)
            getRightView(root.right, l + 1)
        
        levels = dict()
        getRightView(root, 0)
        return [levels[k] for k in levels.keys()]
        
        