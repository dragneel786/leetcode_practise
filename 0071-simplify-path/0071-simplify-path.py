class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        ans = deque()
        for p in paths:
            if(p == '.' or p == ''):
                continue
                
            if(p == '..'):
                if(ans): 
                    ans.pop()
                continue
            
            ans.append(p)
        
        return '/' + "/".join(ans)