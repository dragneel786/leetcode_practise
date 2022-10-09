# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        
        def is_possible(node, k):
            if(not node):
                return False
            
            if(node.val in needed):
                return True
            
            needed.add(k - node.val)
            return is_possible(node.left, k) or\
        is_possible(node.right, k)
            
            
        needed = set()
        return is_possible(root, k)