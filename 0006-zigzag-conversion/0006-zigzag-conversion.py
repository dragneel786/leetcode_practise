class Solution:
    def convert(self, s: str, numRows: int) -> str:
        change_dir = lambda i: i < 0 or i >= numRows
        d = -1
        k = -1
        ans = [[] for _ in range(numRows)]
        for c in s:
            if(change_dir(k + d)):
                d *= -1
            ans[k + d].append(c)
            k += d
        
        return ''.join(map(''.join, ans))
        
        