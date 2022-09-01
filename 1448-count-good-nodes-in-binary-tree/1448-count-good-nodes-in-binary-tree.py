# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = deque([(root, -inf)])
        counts = 0
        
        while(stack):
            node, val = stack.pop()
            if(node.val >= val):
                counts += 1
            
            if(node.left): 
                stack.append((node.left, max(node.val, val)))
            if(node.right):
                stack.append((node.right, max(node.val, val)))
        
        return counts