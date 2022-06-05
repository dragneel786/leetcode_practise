# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def getLeaves(root, l = 0):
            if(not root):
                return -math.inf
            
            r1 = getLeaves(root.left, l)
            r2 = getLeaves(root.right, l)
            idx = 0
            
            if(r1 != -math.inf or r2 != -math.inf):
                idx = max(r1, r2) + 1
            
            if(idx == len(ans)):
                ans.append([])
                
            ans[idx].append(root.val)
            return idx
        
        ans = []
        getLeaves(root)
        return ans