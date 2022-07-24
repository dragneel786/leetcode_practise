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
        encode = lambda x: chr(x + 48)
        
        def doSerial(root):
            if(not root):
                return
            
            output.append(encode(root.val))
            for c in root.children:
                doSerial(c)
            output.append("$")
        
        output = []
        doSerial(root)
        return "".join(output)
        
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        decode = lambda x: ord(x) - 48
        def doDeserial():
            nonlocal idx, data
            if(idx == len(data)):
                return
        
            node = Node(decode(data[idx]), [])
            idx += 1
            while(data[idx] != "$"):
                node.children.append(doDeserial())
            idx += 1
            return node
        
        idx = 0
        return doDeserial()
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))