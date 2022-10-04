# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #Base case
        if(not root):
            return False
        
        if(not root.left and not root.right):
            return (targetSum - root.val) == 0
        
        
        #Recursive body
        if(self.hasPathSum(root.left,\
                           targetSum - root.val)):
            return True
        
        return self.hasPathSum(root.right,\
                               targetSum - root.val)
        