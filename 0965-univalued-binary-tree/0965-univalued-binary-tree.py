# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        stack = deque([])
        val = root.val
        curr = root
        
        while(True):
            if(curr):
                stack.append(curr)
                curr = curr.left
            
            elif(stack):
                node = stack.pop()
                if(node.val != val): return False
                curr = node.right
            
            else:
                return True
    