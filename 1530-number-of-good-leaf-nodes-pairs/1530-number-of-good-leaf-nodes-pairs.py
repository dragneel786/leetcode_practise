# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        
        def dfs(node):
            nonlocal counts
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            print(left, right)
            counts += sum(l + r <= distance for l in left for r in right)
            return [d + 1 for d in left + right if d <= distance]
        
        counts = 0
        dfs(root)
        return counts