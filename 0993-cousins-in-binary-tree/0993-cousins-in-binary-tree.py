# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        check = lambda node: node.val == x or node.val == y
        q = deque([root])
        while(q):
            sibling = cousin = False
            for _ in range(len(q)):
                node = q.popleft()
                
                if(not node):
                    sibling = False
                else:
                    if(check(node)):
                        if(not cousin):
                            cousin = sibling = True
                        else:
                            return not sibling
                        
                    q.append(node.left)
                    q.append(node.right)
                    q.append(None)
                
        return False
        
                
                
            
        