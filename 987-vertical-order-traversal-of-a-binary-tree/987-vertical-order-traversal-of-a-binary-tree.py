# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def traverse_vertical(node, row = 0, col = 0):
            if(not node):
                return
            
            memo[col].append((row, node.val))
            traverse_vertical(node.left, row + 1, col - 1)
            traverse_vertical(node.right, row + 1, col + 1)
            
            
        
        memo = defaultdict(list)
        traverse_vertical(root)
        return [[v for _,v in sorted(memo[key])] for key in sorted(memo.keys())]
        
        
        