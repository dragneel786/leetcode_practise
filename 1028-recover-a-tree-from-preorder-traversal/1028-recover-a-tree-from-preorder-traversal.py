# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def get_number():
            nonlocal stack
            d = 0
            while(stack and stack[0].isdigit()):
                d = (d * 10) + int(stack.popleft())
            return d
        
        def trave_tree():
            nonlocal stack, dash
            if(len(stack) == 0):
                return None
            
            val = get_number()
            node = TreeNode(val)
            if(len(stack) != 0):
                
                old_dash, dash = dash, 0
                while(stack and not stack[0].isdigit()):
                    dash += 1
                    stack.popleft()

                if(old_dash < dash):
                    node.left = trave_tree()

                if(old_dash < dash):
                    node.right = trave_tree()
            
            return node
                
        
        stack = deque(list(traversal))
        dash = 0
        return trave_tree()