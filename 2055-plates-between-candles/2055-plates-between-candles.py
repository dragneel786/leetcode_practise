class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        lcand = [-1 for i in range(n)]
        rcand = [-1 for i in range(n)]
        count = [0 for i in range(n)]
        
        rcurr = lcurr = -1
        tot = 0
        for i in range(n):
            if(s[i] == '|'): 
                lcurr = i
                tot += 1
            
            if(s[n - i - 1] == '|'):
                rcurr = n - i - 1
                
            lcand[i] = lcurr
            rcand[n - i - 1] = rcurr
            count[i] = tot
        
        
        ans = []
        for a, b in queries:
            if(lcand[b] != rcand[a] != -1):
                cb, ca = count[b], count[a-1] if(a - 1 >= 0) else 0
                ans.append(max(0, (lcand[b] - rcand[a] + 1) - (cb - ca)))
            else:
                ans.append(0)
        
        return ans