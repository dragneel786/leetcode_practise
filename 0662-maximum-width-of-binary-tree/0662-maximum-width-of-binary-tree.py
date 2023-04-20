# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = deque([(root, 0)])
        ans = 0
        while(q):
            start = q[0][1]
            end = q[-1][1]
            for _ in range(len(q)):
                node, idx = q.popleft()
                child_idx = 2 * (idx - 1)
                if(node.left):
                    q.append((node.left, child_idx + 1))
                
                if(node.right):
                    q.append((node.right, child_idx + 2))
            
            ans = max(end - start + 1, ans)
            
        return ans