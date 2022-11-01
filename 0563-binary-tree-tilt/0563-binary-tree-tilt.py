# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        
        def find_Tilt(node):
            nonlocal ans
            if(not node):
                return 0

            left_sum = find_Tilt(node.left)
            right_sum = find_Tilt(node.right)
            ans += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val
        
        ans = 0
        find_Tilt(root)
        return ans