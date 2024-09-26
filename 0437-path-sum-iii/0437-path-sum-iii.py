# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        def dfs(root, prevSum, sum):
            if not root:
                return 
            currSum = prevSum + root.val
            if currSum - sum in rec:
                self.count += rec[currSum - sum]
            if currSum in rec:
                rec[currSum] += 1
            else:
                rec[currSum] = 1
            dfs(root.left, currSum, sum)
            dfs(root.right, currSum, sum)
            rec[currSum] -= 1

        self.count = 0
        rec = {0:1}
        dfs(root, 0, sum)
        return self.count