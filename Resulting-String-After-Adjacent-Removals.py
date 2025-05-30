class Solution:
    def resultingString(self, s: str) -> str:
        def is_circular(a, b):
            if a > b:
                return is_circular(b, a)
            
            aord, bord = ord(a) - 97, ord(b) - 97
            if aord + 1 == bord:
                return True
            
            if a == 'a' and b == 'z':
                return True
            
            return False
            


        st = deque()
        for c in s:
            if st and is_circular(st[-1], c):
                st.pop()
            else:
                st.append(c)
        
        return ''.join(st)