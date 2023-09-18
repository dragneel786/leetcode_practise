# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def sumed(node, li = []):
            nonlocal sums
            if(not node):
                return
            
            for i in range(len(li)):
                li[i] -= 1
                if li[i] == 0:
                    sums += node.val
                    
            if(node.val % 2 == 0):
                li.append(2)
            
            sumed(node.left, li[:])
            sumed(node.right, li[:])
        
        sums = 0
        sumed(root)
        return sums
            