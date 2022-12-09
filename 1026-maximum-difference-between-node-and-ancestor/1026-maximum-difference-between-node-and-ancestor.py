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
            
            ans = max(abs(minv - node.val),\
                      abs(maxv - node.val),\
                      ans)
            
            maxv = max(maxv, node.val)
            minv = min(minv, node.val)
            find_diff(node.left, minv, maxv)
            find_diff(node.right, minv, maxv)
            
        ans = 0
        find_diff(root, root.val, root.val)
        return ans