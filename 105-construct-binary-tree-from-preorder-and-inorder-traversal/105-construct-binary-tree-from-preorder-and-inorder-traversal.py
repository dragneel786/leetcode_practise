# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def builder(ino, pre, stop = None):
            if(not ino or stop == ino[-1]):
                return None
            
            node = TreeNode(pre.pop())
            node.left = builder(ino, pre, node.val)
            if(ino and node.val == ino[-1]):
                ino.pop()
            node.right = builder(ino, pre, stop)
            return node
        
        inorder.reverse()
        preorder.reverse()
        return builder(inorder, preorder)
    
        
        
            