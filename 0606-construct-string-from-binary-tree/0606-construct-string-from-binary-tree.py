# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if(not root):
            return ''
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        ret = ''
        if(len(right)):
            ret = "({})({})".format(left, right)
        elif(len(left)):
            ret = "({})".format(left)
        
        return str(root.val) + ret