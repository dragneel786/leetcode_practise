class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        res = []
        for log in logs:
            s = set([log[1], log[2]])
            for r in res:
                if(log[1] in r or log[2] in r):
                    s.update(r)
            
            if(len(s) == n):
                return log[0]
            res.append(s)
        
        return -1
                    
            
                
            