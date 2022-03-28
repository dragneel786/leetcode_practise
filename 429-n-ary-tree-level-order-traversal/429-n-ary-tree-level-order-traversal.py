"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if(not root):
            return res
        
        st = deque()
        st.append(root)
        while(len(st)):
            level = []
            for _ in range(len(st)):
                node = st.pop()
                for n in node.children:
                    st.appendleft(n)
                level.append(node.val)
            
            res.append(level)
        
        return res
        