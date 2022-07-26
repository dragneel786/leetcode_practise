# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        
        def findLongest(child, parent):
            nonlocal res
            if(not child):
                return 1
            
            l1 = findLongest(child.left, child)
            l2 = findLongest(child.right, child)
            if(not parent or parent.val + 1 != child.val):
                res = max(l1, l2, res)
                return 1
            
            return max(l1, l2) + 1
                
        
        res = 0
        findLongest(root, None)
        return res