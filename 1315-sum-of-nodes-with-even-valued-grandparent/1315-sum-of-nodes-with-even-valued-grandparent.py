# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def add(node):
            nonlocal sums
            if not node:
                return 
            
            if(node.left):
                sums += node.left.val
            
            if(node.right):
                sums += node.right.val
        
        def sumed(node):
            if(not node):
                return
            
            if(node.val % 2 == 0):
                add(node.left)
                add(node.right)
            
            sumed(node.left)
            sumed(node.right)
        
        sums = 0
        sumed(root)
        return sums
            