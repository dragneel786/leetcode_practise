# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildThem(pre, ino):
            nonlocal p
            if(not ino):
                return None
            
            newNode = TreeNode(pre[p])
            idx = getIndex(pre[p], ino)
            p += 1
            newNode.left = buildThem(pre, ino[:idx])
            newNode.right = buildThem(pre, ino[idx + 1:])
            return newNode
        
        def getIndex(v, arr):
            for i,a in enumerate(arr):
                if(a == v):
                    return i
            
            
        p = 0
        return buildThem(preorder, inorder)
            