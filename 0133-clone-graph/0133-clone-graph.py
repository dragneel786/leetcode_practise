"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def clone_graph(node, indexed = dict()):
            if(not node):
                return None
            
            if(node.val in indexed):
                return indexed[node.val]
            
            indexed[node.val] = Node(node.val)
            for nei in node.neighbors:
                indexed[node.val]\
                .neighbors\
                .append(clone_graph(nei, indexed))
            
            return indexed[node.val]
        
        return clone_graph(node)
                
            
        