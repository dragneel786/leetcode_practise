# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def postorder(node):
            if(not node):
                return 0
            
            ret = postorder(node.left) +\
            postorder(node.right) +\
            node.val
            sums.append(ret)
            return ret
        
        sums = []
        total = postorder(root)
        best = 0
        for s in sums:
            best = max(best, s * (total - s))
        
        return best % (10 ** 9 + 7)