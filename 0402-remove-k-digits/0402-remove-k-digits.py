class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = deque()
        for c in num:
            while(k and st and int(st[-1]) > int(c)):
                st.pop()
                k -= 1
            
            st.append(c)
        
        for _ in range(k):
            st.pop()
        
        while(st and st[0] == '0'):
            st.popleft()
        
        return ''.join(st) if(st) else '0'
        
        
                