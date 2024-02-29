# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        is_even = True
        q = deque([root])
        while(q):
            prev = -inf if(is_even) else inf
            for _ in range(len(q)):
                node = q.popleft()
                val = node.val
                if(is_even and (val % 2 == 0 or val <= prev)):
                    return False

                elif(not is_even and (val % 2 == 1 or val >= prev)):
                    return False

                if(node.left):
                    q.append(node.left)

                if(node.right):
                    q.append(node.right)
                
                prev = val
            is_even = not is_even
        
        
        return True