class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def calc(string, sub, val):
            nonlocal tot
            st = deque()
            for c in string:
                st.append(c)
                if len(st) > 1 and st[-1] == sub[-1] and st[-2] == sub[-2]:
                    st.pop()
                    st.pop()
                    tot += val
            
            return ''.join(st)
        
        fsub, ssub = 'ab', 'ba'
        if x < y:
            fsub, ssub = ssub, fsub
            x, y = y, x
        
        tot = 0
        calc(calc(s, fsub, x), ssub, y)
        return tot

