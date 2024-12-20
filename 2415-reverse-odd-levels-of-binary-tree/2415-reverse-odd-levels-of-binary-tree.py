# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        odd = True
        lvals = []
        while(q):
            for _ in range(len(q)):
                node = q.popleft()
                if not odd:
                    node.val = lvals.pop()
                
                if node.left:
                    q.append(node.left)
                    if odd:
                        lvals.append(node.left.val)
                
                if node.right:
                    q.append(node.right)
                    if odd:
                        lvals.append(node.right.val)
                
            odd = not odd 
            
        return root
                
                
                