# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def compare(left, right):
            for a, b in zip_longest(left, right, fillvalue=-1):
                if(a < b):
                    return left
                
                if(a > b):
                    return right
                
            return left
            
        
        def order(node, values = []):
            nonlocal res
            if(not node):
                return
            
            values = [node.val] + values
            print(values)
            order(node.left, values)
            order(node.right, values)
            if(not node.left and not node.right):
                # print("Entered Here", values)
                res = compare(values, res)
        
        
        
        res = [26]
        ans = []
        order(root)
        for v in res:
            ans.append(chr(97 + v))
        
        return ''.join(ans)
            
            
        