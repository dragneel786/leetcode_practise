# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def find_node(node, level):
            nonlocal max_level, sub_node
            if(not node):
                return level
            
            left = find_node(node.left, level + 1)
            right = find_node(node.right, level + 1)
            if(left == right and max_level <= left):
                max_level = left
                sub_node = node
            
            return max(left, right)
            
        
        max_level = 0
        sub_node = root
        find_node(root, 1)
        return sub_node
        