# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        def find_diff(node, minv, maxv):
            nonlocal ans
            if(not node):
                return
            
            if(node.left):
                find_diff(node.left,\
                          min(minv, node.left.val),\
                          max(maxv, node.left.val))
            
            if(node.right):
                find_diff(node.right,\
                          min(minv, node.right.val),\
                          max(maxv, node.right.val))
            
            ans = max(abs(minv - node.val),\
                      abs(maxv - node.val),\
                      ans)
            
        
        ans = 0
        find_diff(root, root.val, root.val)
        return ans