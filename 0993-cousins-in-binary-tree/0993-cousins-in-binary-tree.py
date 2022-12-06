# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        q = deque([root])
        parent = dict()
        while(q):
            level = set()
            for _ in range(len(q)):
                ele = q.popleft()
                level.add(ele.val)
                
                if(ele.left):
                    parent[ele.left.val] = ele.val
                    q.append(ele.left)
                
                if(ele.right):
                    parent[ele.right.val] = ele.val
                    q.append(ele.right)
            
            if(x in level and y in level):
                return parent[x] != parent[y]
                
        
        return False
                
                
            
        