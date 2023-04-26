# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(node, rev):
            if(not node):
                return 
            
            if(node.left == node.right == None):
                return
            
            if(rev):
                ans.append(node.val)
                if(node.left):
                    traverse(node.left, rev)
                else:
                    traverse(node.right, rev)
            else:
                if(node.right):
                    traverse(node.right, rev)
                else:
                    traverse(node.left, rev)
                ans.append(node.val)
        
        
        def dfs(node):
            if(not node):
                return 
            
            if(node.left == node.right == None):
                ans.append(node.val)
                return
            
            dfs(node.left)
            dfs(node.right)
        
        
        ans = [root.val]
        traverse(root.left, True)
        dfs(root.left)
        dfs(root.right)
        traverse(root.right, False)
        return ans
                
        
            
        
        