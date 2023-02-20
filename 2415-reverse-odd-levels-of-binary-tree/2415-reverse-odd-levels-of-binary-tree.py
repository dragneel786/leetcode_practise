# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_que = deque([root])
        val_que = deque([root.val])
        level = 0
        while(node_que):
            new_lev = deque()
            for _ in range(len(node_que)):
                node = node_que.popleft()
                val = -1
                if(level % 2 == 0):
                    val = val_que.popleft()
                else:
                    val = val_que.pop()
    
                node.val = val            
                if(node.left):
                    node_que.append(node.left)
                    new_lev.append(node.left.val)
                
                if(node.right):
                    node_que.append(node.right)
                    new_lev.append(node.right.val)
                
            level += 1
            val_que = new_lev
                    
        return root