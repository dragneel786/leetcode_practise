# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        que = deque([(root, 0)])
        elms = defaultdict(list)
        ans = []
        while(root and que):
            for _ in range(len(que)):
                node, level = que.popleft()
                elms[level].append(node.val)
                
                if(node.left):
                    que.append((node.left, level + 1))
                
                if(node.right):
                    que.append((node.right, level - 1))
                
        
        for k in sorted(elms.keys(), reverse=True):
            ans.append(elms[k])
        return ans