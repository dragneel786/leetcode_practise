# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def count_pseudo(root, path = 0):
            nonlocal res
            if(not root):
                return
            
            path ^= (1 << root.val)
            count_pseudo(root.left, path)
            count_pseudo(root.right, path)
            
            if(not root.left and not root.right):
                res += (path & (path - 1)) == 0
        
        res = 0
        count_pseudo(root)
        return res
            