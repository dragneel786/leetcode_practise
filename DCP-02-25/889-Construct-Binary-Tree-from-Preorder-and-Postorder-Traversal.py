# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def construct():
            nonlocal preorder, postorder
            if not preorder:
                return None

            print(preorder, postorder)
            node = TreeNode(preorder.pop(0))
            if node.val == postorder[0]:
                postorder.pop(0)
                return node
            
            node.left = construct()
            if node.val != postorder[0]:
                node.right = construct()
            
            postorder.pop(0) 
            return node

        return construct()