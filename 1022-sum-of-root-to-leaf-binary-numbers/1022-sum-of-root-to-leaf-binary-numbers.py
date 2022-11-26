# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def sums(root, curr_val):
            nonlocal ans
            if(root):
                val = (curr_val << 1) | root.val
                if(not root.left and not root.right):
                    ans += val
                    return
                
                sums(root.left, val)
                sums(root.right, val)
        
        ans = 0
        sums(root, 0)
        return ans
        