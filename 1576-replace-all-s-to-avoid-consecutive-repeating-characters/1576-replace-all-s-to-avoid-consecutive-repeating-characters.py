class Solution:
    def modifyString(self, s: str) -> str:
        chars = ['a', 'b', 'c']
        ans = []
        j = 0
        n = len(s)
        
        condition = lambda p: (ans and ans[-1] == chars[j]) or\
        (p < n - 1 and chars[j] == s[p + 1])
        
        
        for i in range(n):
            if(s[i] == '?'):
                while(condition(i)):
                    j = (j + 1) % 3

                ans.append(chars[j])
            
            else:
                ans.append(s[i])
        
        return ''.join(ans)