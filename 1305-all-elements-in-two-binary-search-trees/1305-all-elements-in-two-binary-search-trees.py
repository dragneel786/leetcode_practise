# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def preorder(node):
            if(not node):
                return []
            
            left = preorder(node.left)
            middle = [node.val]
            right = preorder(node.right)
            return left + middle + right
        
        left = preorder(root1)
        right = preorder(root2)
        i = j = 0
        res = []
        while(i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        while(i < len(left)):
            res.append(left[i])
            i += 1
        
        while(j < len(right)):
            res.append(right[j])
            j += 1
        
        return res
        
        
            