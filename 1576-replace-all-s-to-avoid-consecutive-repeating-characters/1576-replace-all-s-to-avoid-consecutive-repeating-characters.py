class Solution:
    def modifyString(self, s: str) -> str:
        chars = ['a', 'b', 'z']
        ans = []
        j = 0
        n = len(s)
        
        condition = lambda p: (ans and ans[-1] == chars[j]) or\
        (p < n - 1 and chars[j] == s[p + 1])
        
        
        for i in range(n):
            ch = s[i]
            if(s[i] == '?'):
                while(condition(i)):
                    j = (j + 1) % 3
                ch = chars[j]
            
            ans.append(ch)
        
        return ''.join(ans)