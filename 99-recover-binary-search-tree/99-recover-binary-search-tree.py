# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def findMis(root, first, second, prev = [None]):
            if(not root):
                return
            
            findMis(root.left, first, second, prev)
            if(prev[0]):
                if(not first[0] and prev[0].val > root.val):
                    first[0] = prev[0]
                if(first[0] and prev[0].val > root.val):
                    second[0] = root
            prev[0] = root
            findMis(root.right, first, second, prev)
        
        first = [None]
        second = [None]
        findMis(root, first, second)
        first[0].val, second[0].val = second[0].val, first[0].val
                