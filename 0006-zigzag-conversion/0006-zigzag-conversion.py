class Solution:
    def convert(self, s: str, numRows: int) -> str:
        change_dir = lambda i: i < 0 or i >= numRows
        d = 1
        k = 0
        ans = [[] for _ in range(numRows)]
        for c in s:
            if(change_dir(k)):
                d *= -1
                k += (d * 2)
            ans[k].append(c)
            k += d
        
        return ''.join(map(''.join, ans))
            
            
            
        
        return ans
        
        