# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(not root.left and not root.right):
            return True
        
        q1 = deque()
        q2 = deque()
        q1.appendleft(root.left)
        q2.appendleft(root.right)
        while(q1 and q2):
            if(len(q1) != len(q2)):
                return False
            
            for _ in range(len(q1)):
                n1 = q1.pop()
                n2 = q2.pop()
                if((not n1 and n2) or (not n2 and n1)):
                    return False
                
                if((n1 and n2) and n1.val != n2.val):  
                    return False
                
                if(n1):
                    q1.appendleft(n1.left)
                    q1.appendleft(n1.right)

                if(n2):
                    q2.appendleft(n2.right)
                    q2.appendleft(n2.left)
                    
        return True