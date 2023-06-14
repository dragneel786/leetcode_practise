# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def in_ord(node):
            nonlocal prev
            if(not node):
                return inf
            
            left = in_ord(node.left)
            val = inf
            if(prev): val = abs(prev.val - node.val)
            prev = node
            right = in_ord(node.right)
            
            return min(left, right, val)
        
        prev = None
        return in_ord(root)