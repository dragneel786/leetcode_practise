# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def get_max_idx(values):
            max_idx = max_val = -1
            for i, v in enumerate(values):
                if(max_val < v):
                    max_idx = i
                    max_val = v
            
            return max_idx
                
        
        def get_tree(node):
            if not node:
                return []
            
            left = get_tree(node.left)
            right = get_tree(node.right)
            return left + [node.val] + right
    
        
        def construct_tree(values):
            if(not values):
                return None
            
            max_idx = get_max_idx(values)
            node = TreeNode(values[max_idx])
            node.left = construct_tree(values[:max_idx])
            node.right = construct_tree(values[max_idx + 1:])
            return node
        
        
        return construct_tree(get_tree(root) + [val])
            
            
            
            
            
        