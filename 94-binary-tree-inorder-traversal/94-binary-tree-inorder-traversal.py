# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def inorder(ele):
            if(not ele):
                return
            inorder(ele.left)
            res.append(ele.val)
            inorder(ele.right)
        
        inorder(root)
        return res
        