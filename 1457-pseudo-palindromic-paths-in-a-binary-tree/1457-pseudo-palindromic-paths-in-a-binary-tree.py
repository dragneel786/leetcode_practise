# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        values = [0] * 10
        
        count_odds = lambda values: sum(v % 2 for v in values)
        
        def count_pseudo(root):
            if(not root):
                return 0
            
            values[root.val] += 1
            
            res = count_pseudo(root.left)
            res += count_pseudo(root.right)
            
            if(not root.left and not root.right):
                res += count_odds(values) <= 1
            
            values[root.val] -= 1
            
            return res
    
        return count_pseudo(root)
            