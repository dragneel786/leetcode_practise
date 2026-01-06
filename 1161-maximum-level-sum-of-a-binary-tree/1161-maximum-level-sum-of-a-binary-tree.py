# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        level = max_level = 0
        max_val = -inf
        while(que):
            level += 1
            tot = 0
            for _ in range(len(que)):
                node = que.popleft()
                tot += node.val
                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)

            if tot > max_val:
                max_level = level
                max_val = tot
        
        return max_level
                