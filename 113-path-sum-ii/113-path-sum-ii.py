# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def root_to_leaf(root, path_sum = 0, op = []):
            nonlocal targetSum
            if(not root): return
            
            op.append(root.val)
            
            if(root.left or root.right):
                root_to_leaf(root.left,
                             path_sum + root.val, op)

                root_to_leaf(root.right,
                             path_sum + root.val, op)
            
            elif(path_sum + root.val == targetSum):
                res.append(op[:])
                
            op.pop()
            
        res = []
        root_to_leaf(root)
        return res
            