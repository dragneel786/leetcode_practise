# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, node: Optional[TreeNode]) -> List[int]:
        
        if(not node):
            return []
        
        ans = []
        if(node.left and not node.right):
            ans.append(node.left.val)
        
        if(node.right and not node.left):
            ans.append(node.right.val)
        
        left = self.getLonelyNodes(node.left)
        right = self.getLonelyNodes(node.right)
        return ans + left + right