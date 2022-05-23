"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if(not node):
            return None
        
        visited = defaultdict(lambda:None)
        def cloneIt(org):
            if(visited[org.val]):
                return visited[org.val]
            
            copy = Node()
            copy.val = org.val
            visited[org.val] = copy
            for node in org.neighbors:
                copy.neighbors.append(cloneIt(node))
            
            return copy
        
        return cloneIt(node)
            