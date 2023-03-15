# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        def copy(node):
            if(not node):
                return None
            
            new_node = NodeCopy(node.val)
            node_map[node] = new_node
            new_node.left = copy(node.left)
            new_node.right = copy(node.right)
            return new_node
        
        node_map = defaultdict(lambda:None)
        new_root = copy(root)
        for n1, n2 in list(node_map.items()):
            n2.random = node_map[n1.random]
        
        return new_root
        