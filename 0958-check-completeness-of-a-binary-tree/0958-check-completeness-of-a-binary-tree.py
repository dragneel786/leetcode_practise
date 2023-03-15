# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        q = deque([root])
        h = 0
        while(q):
            n = len(q)
            if(q[0] and n < 2 ** h):
                return False
            
            is_null = False
            for _ in range(n):
                node = q.popleft()
                if(not node):
                    is_null = True
                    continue
                    
                if(node and is_null):
                    return False
               
                q.append(node.left)
                q.append(node.right)
            
            h += 1
        
        return True