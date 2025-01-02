# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        def get_min(node):
            nonlocal min1, min2
            if not node:
                return
            
            if min1 > node.val:
                min2 = min1
                min1 = node.val
            
            elif min2 > node.val and node.val != min1:
                min2 = node.val

            # print(min1, min2)
            get_min(node.left)
            get_min(node.right)
        
        min1 = min2 = inf
        get_min(root)
        return min2 if min2 != inf else -1
