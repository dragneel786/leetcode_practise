# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        dummy_root = TreeNode(left=root)
        stack = deque([(dummy_root, depth)])
        
        while(stack):
            node, dep = stack.pop()
            
            if(dep == 1):
                left, right = node.left, node.right
                node.left = TreeNode(val, left=left)
                node.right = TreeNode(val,right=right)
                continue
            
            if(node.right):
                stack.append((node.right, dep - 1))
            
            if(node.left):
                stack.append((node.left, dep - 1))
        
        return dummy_root.left
        
        