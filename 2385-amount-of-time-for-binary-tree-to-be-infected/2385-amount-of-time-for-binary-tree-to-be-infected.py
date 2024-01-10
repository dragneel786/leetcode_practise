# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        def copy_tree(node, parent = None):
            nonlocal infection_start
            if(not node):
                return None
            
            new_node = TreeNode(node.val, parent = parent)
            new_node.left = copy_tree(node.left, new_node)
            new_node.right = copy_tree(node.right, new_node)
            if(new_node.val == start):
                infection_start = new_node
                
            return new_node
        
        
        infection_start = None
        root = copy_tree(root)
        q = deque([infection_start])
        time = -2
        while(q):
            for _ in range(len(q)):
                node = q.popleft()           
                if(node is None or\
                   node.val == -1):
                    continue
                
                # print(node.val, end=" ")
                node.val = -1
                q.append(node.left)
                q.append(node.right)
                q.append(node.parent)
            
            time += 1
        
        return time
        
        
        