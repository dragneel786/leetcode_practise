# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = Counter()
        
        def init_level_sum(node, level):
            if(not node):
                return
            
            level_sum[level] += node.val
            init_level_sum(node.left, level + 1)
            init_level_sum(node.right, level + 1)
        
        def init_nodes(node, level):
            if(not node):
                return
            
            tot = 0
            if(node.left):
                tot += node.left.val
            
            if(node.right):
                tot += node.right.val
            
            if(node.left):
                node.left.val = level_sum[level + 1] - tot
            
            if(node.right):
                node.right.val = level_sum[level + 1] - tot
            
            init_nodes(node.left, level + 1)
            init_nodes(node.right, level + 1)
        
        init_level_sum(root, 0)
        # print(level_sum)
        init_nodes(root, 0)
        root.val = 0
        return root
            
            
            
        
        
        