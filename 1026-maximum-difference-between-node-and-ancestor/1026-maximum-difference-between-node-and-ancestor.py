# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        def find_diff(node, minv, maxv):
            if(not node):
                return maxv - minv
            
            maxv = max(maxv, node.val)
            minv = min(minv, node.val)
            left = find_diff(node.left, minv, maxv)
            right = find_diff(node.right, minv, maxv)
            
            return max(left, right)
            
        return find_diff(root, root.val, root.val)