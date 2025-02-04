# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        
        def pre_order(node):
            nonlocal start
            if node is None:
                return True
            
            if node.val != voyage[start]:
                return False
            
            start += 1
            if pre_order(node.left) and pre_order(node.right):
                return True
            
            elif pre_order(node.right) and pre_order(node.left):
                flipped.append(node.val)
                return True
            
            return False
        
        start = 0
        flipped = []
        if not pre_order(root):
            return [-1]

        return flipped



            