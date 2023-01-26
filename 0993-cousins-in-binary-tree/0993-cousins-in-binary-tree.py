# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        def is_cousins(node, p, curr_level):
            nonlocal level
            if(not node or (level and curr_level > level[0])):
                return False
            
            if(node.val == x or node.val == y):
                if(not level):
                    level = (curr_level, p)
                    return False
                
                return level[0] == curr_level and level[1] != p
            
            return is_cousins(node.left, node.val, curr_level + 1) or\
        is_cousins(node.right, node.val, curr_level + 1)
        
        
        level = None
        return is_cousins(root, -1, 0)
        
                
                
            
        