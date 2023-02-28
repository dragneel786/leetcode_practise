# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def traverse_and_find(node):
            if(not node):
                return ""
            
            left = traverse_and_find(node.left)
            right = traverse_and_find(node.right)
            ret = str(node.val) + f'({left}|{right})'
            
            if(subtrees[ret] == 1):
                result.append(node)
            
            subtrees[ret] += 1
            return ret
        
        subtrees = Counter()
        result = []
        traverse_and_find(root)
        return result
        