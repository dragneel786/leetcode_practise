# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        lev= 0
        temp = root
        while(temp):
            temp = temp.left
            lev += 1
        
        total = [0]
        total[0] = (2 ** lev) - 1
        
        def findLastNode(root, curr = 1):
            if(not root):
                if(curr == lev):
                    total[0] -= 1
                return
            
            findLastNode(root.right, curr + 1)
            findLastNode(root.left, curr + 1)
            if(root and curr == lev):
                return
        
        findLastNode(root)
        return total[0]