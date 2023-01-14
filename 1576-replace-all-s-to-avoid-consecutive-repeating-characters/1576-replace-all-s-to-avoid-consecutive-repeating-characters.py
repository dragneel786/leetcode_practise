class Solution:
    def modifyString(self, s: str) -> str:
        ans = []
        n = len(s)
        for i, c in enumerate(s):
            nxt = s[i + 1] if(i < n - 1) else '#'
            prev = ans[-1] if(ans) else '?'
            ch = c if(c != '?') else {'a', 'b', 'c'}\
            .difference({prev, nxt}).pop()
            ans.append(ch)
        
        return ''.join(ans)