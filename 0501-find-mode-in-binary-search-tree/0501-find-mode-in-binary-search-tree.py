# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def mode(node):
            nonlocal max_c
            if not node:
                return
            
            mode(node.left)
            counts[node.val] += 1
            max_c = max(counts[node.val], max_c)
            mode(node.right)
            
        counts = Counter()
        max_c = 0
        mode(root)
        return [k for k, v in counts.items() if v == max_c]