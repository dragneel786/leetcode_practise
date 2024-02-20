# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        def get_root(node, val):
            nonlocal limit
            if(not node):
                return None, val
            
            left, right = node.left, node.right
            new_val = node.val + val
            node.left, sumL = get_root(node.left, new_val)
            node.right, sumR = get_root(node.right, new_val)
            
            ret_val = new_val
            if(right and left):
                ret_val = max(sumL, sumR)
            
            elif(left):
                ret_val = sumL
            
            elif(right):
                ret_val = sumR
            
            if(ret_val < limit):
                return None, ret_val
            
            return node, ret_val
            
        
        node = get_root(root, 0)[0]
        return node