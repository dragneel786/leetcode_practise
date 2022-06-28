# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        postfix = self.convertToPostfix(s)
        print(postfix)
        tree = deque()
        s = deque()
        for p in postfix:
            if(p.isdigit()):
                tree.append(Node(p))
            else:
                o = Node(p)
                o.right, o.left = tree.pop(), tree.pop()
                tree.append(o)
        return tree[-1]
            
        
    def convertToPostfix(self, s):
        def popV():
            o = ope.pop()
            v2, v1 = opr.pop(), opr.pop()
            opr.append(v1 + v2 + o)
            
        ope = deque()
        opr = deque()
        weight = {"+": 1, "-":1, "*":2, "/":2, "(":0}
        for c in s:
            if(c.isdigit()):
                opr.append(c)
            elif(c == "("):
                ope.append(c)
            elif(c == ")"):
                while(ope[-1] != "("):
                    popV()
                ope.pop()
            else:
                while(ope and weight[ope[-1]] >= weight[c]):
                    popV()
                ope.append(c)
                
        while(ope):
            popV()
                
        return opr.pop()
    
            
                
                
                    
            
        