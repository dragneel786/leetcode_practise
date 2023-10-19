class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def type_it(w):
            q = deque()
            for c in w:
                if(c != '#'):  
                    q.append(c)
                elif(q):
                    q.pop()
            
            return ''.join(q)
        
        return type_it(s) == type_it(t)
        
        
        
                