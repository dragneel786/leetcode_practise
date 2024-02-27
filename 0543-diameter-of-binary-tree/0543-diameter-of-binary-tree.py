# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def find_ans(node):
            nonlocal longest
            if(not node):
                return 0
            
            left = find_ans(node.left)
            right = find_ans(node.right)
            longest = max(longest, 1 + left + right)
            return 1 + max(left, right)
        
        longest = 1
        find_ans(root)
        return longest - 1