class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = Counter(s)
        st = deque()
        curr = set()
        for c in s:
            if(c in curr):
                counts[c] -= 1
                continue
                
            while(st and counts[st[-1]] > 1 and st[-1] >= c):
                ch = st.pop()
                counts[ch] -= 1
                curr.remove(ch)
            
            st.append(c)
            curr.add(c)
            
        return ''.join(st)
            