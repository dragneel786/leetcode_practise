# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        0: left is not processed
        1: left processed
        '''
        if(not root): return []
        
        stack = deque([(root, 0)])
        res = []
        
        while(stack):
            node, op = stack.pop()
            
            if(not op and node.left):
                stack.append((node, 1))
                stack.append((node.left, 0))
            else:
                res.append(node.val)
                if(node.right): stack.append((node.right, 0))
        
        return res
                
                    
        
        
        