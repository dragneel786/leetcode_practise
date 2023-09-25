# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def create(li):
            if(not li):
                return None
            
            if(len(li) == 1):
                return TreeNode(li[0])
            
            node = TreeNode(li[0])
            for i in range(0, len(li) + 1):
                if(i == len(li)):
                    break
                    
                if(li[i] > li[0]):
                    break
            
            node.left = create(li[1:i])
            node.right = create(li[i:])
        
            return node
    
        return create(preorder)