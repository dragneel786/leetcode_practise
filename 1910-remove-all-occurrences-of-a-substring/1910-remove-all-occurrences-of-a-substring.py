class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
#         ans = deque()
#         idx = 0
#         n = len(part)
#         for c in s + '-':
#             if(idx == n):
#                 for _ in range(n):
#                     ans.pop()
#                 idx = 0
            
#             if(ans and ans[-1] == part[idx]):
#                 idx += 1
#             else:
#                 idx = 1 if(ans and ans[-1] == part[0]) else 0
            
#             ans.append(c)
        
#             print(ans, idx)
#         return ''.join(ans)
        n=len(part)
        while part in s:
            i=s.index(part)
            s=s[:i]+s[i+n:]
        return s
                
            
                
                
            
            