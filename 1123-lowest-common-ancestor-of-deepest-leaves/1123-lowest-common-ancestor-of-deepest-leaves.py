# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None
        
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node, parent = None, l = 0):
            if(not node):
                return 0
            
            node.parent = parent
            lmap[l].append(node)
            return max(traverse(node.left, node, l + 1),\
                      traverse(node.right, node, l + 1)) + 1
        
        lmap = defaultdict(list)
        max_depth = traverse(root)
        nodes = set(lmap[max_depth - 1])
        while(len(nodes) != 1):
            new_nodes = set()
            for e in nodes:
                new_nodes.add(e.parent)
            nodes = new_nodes
        
        return list(nodes)[0]
        