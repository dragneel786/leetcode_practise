# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.appendleft([root, 0])
        res = 0
        while(len(q)):
            # print(q)
            start = q[-1][1]
            end = q[0][1]
            for _ in range(len(q)):
                node = q.pop()
                idx = 2 * (node[1] - start)
                if(node[0].left):
                    q.appendleft([node[0].left, idx + 1])
                if(node[0].right):
                    q.appendleft([node[0].right, idx + 2])
                
                
            res = max(res, end - start + 1)
        
        return res
        