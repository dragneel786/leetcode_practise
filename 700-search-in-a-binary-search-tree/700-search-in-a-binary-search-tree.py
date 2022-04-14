# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if(not root):
            return None
        
        if(root.val == val):
            return root
        
        ret1 = self.searchBST(root.left, val)
        ret2 = self.searchBST(root.right, val)
        
        if(ret1):
            return ret1
        if(ret2):
            return ret2
        else:
            return None
        