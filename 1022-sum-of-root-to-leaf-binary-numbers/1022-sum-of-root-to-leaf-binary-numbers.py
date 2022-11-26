# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        que = deque([(root, str(root.val))])
        ans = 0
                     
        while(que):
            for _ in range(len(que)):
                node, val = que.popleft()
                
                if(not node.left and not node.right):
                    ans += int(val, 2)
                    continue
                
                if(node.left):
                    que.append((node.left, val + str(node.left.val)))
                if(node.right):
                    que.append((node.right, val + str(node.right.val)))
            
        return ans
        