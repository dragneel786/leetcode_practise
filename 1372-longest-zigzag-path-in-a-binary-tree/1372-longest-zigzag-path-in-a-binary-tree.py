# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def get_max(node, val=0, s=''):
            nonlocal max_ans
            if(not node):
                return 
            
            max_ans = max(max_ans, val)
            left = right = 1
            if(not s or s == 'r'):
                left = val + 1
            
            if(not s or s == 'l'):
                right = val + 1

            get_max(node.left, left, 'l')
            get_max(node.right, right, 'r')
        
        max_ans = 0
        get_max(root)
        return max_ans
        
        