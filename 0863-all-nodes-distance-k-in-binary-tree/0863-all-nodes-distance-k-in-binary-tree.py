# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node, par = None):
            if(not node):
                return
            
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
        
        def bfs():
            q = deque([(target, 0)])
            seen = set([target.val])
            
            while(q):
                node, dis = q.popleft()
                if(dis == k):
                    res.append(node.val)
                    
                for no in [node.left, node.right, parent[node]]:
                    if(no and no.val not in seen):
                        seen.add(no.val)
                        q.append((no, dis + 1))
        parent = {}        
        dfs(root)
        res = []
        bfs()
        return res
                        
            
            
            
            
            