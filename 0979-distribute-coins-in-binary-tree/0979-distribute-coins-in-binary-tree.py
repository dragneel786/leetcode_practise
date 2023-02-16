# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def min_moves(node):
            nonlocal ans
            if(not node):
                return 0
            
            left = min_moves(node.left)
            right = min_moves(node.right)
            ret = node.val + left + right - 1
            # ex = (node.val + e1 + e2 - 1)
            # ne = abs(ex - n1 + n2)
            ans += abs(ret)
            return ret
        
        
        
        ans = 0
        min_moves(root)
        return ans