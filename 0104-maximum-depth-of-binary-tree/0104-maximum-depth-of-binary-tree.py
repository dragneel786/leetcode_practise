# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        ans = 0
        while(q):
            node, l = q.pop()
            if(not node):
                ans = max(ans, l)
            else:
                q.append((node.left, l + 1))
                q.append((node.right, l + 1))
    
        return ans
            
            
                