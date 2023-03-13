# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        mins = [-inf, -1]
        level = 1
        while(q):
            tot = 0
            for _ in range(len(q)):
                node = q.popleft()
                tot += node.val
                if(node.left):
                    q.append(node.left)
                
                if(node.right):
                    q.append(node.right)
            
            if(mins[0] < tot):
                mins = [tot, level]
            
            level += 1
        
        return mins[-1]