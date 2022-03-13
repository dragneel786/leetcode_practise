from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        lookup = {')': '(', '}':'{', ']':'['}
        for b in s:
            if(b in lookup and (len(st) == 0 or st[-1] != lookup[b])):
                return False
            
            if(b not in lookup):
                st.append(b)
            else:
                st.pop()
    
        return len(st) == 0
            
                