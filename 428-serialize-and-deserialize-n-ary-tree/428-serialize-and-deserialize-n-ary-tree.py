"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if(not root):
            return "()"
        
        convertInString = lambda lst: "(" + ",".join([str(e.val) for e in lst]) + ")"
        res = ""
        q = deque([[root]])
        while(q):
            temp = []
            for _ in range(len(q)):
                poped = q.popleft()
                for p in poped:
                    q.append(p.children if(p.children) else [])
                temp.append(convertInString(poped))
            res += ".".join(temp)
            res += "|"
        return res[:-1]
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        convertInList = lambda string: string[1:-1].split(",")
        
        levels = deque(data.split("|"))
        node = convertInList(levels.popleft())
        if(not node[0]):
            return None
        root = Node(int(node[0]), [])
        q = deque([root])
        while(levels):
            nextLevel = levels.popleft().split(".")
            for i in range(len(q)):
                node = q.popleft()
                childs = convertInList(nextLevel[i])
                if(childs[0]):
                    for c in childs:
                        temp = Node(int(c), [])
                        q.append(temp)
                        node.children.append(temp)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))