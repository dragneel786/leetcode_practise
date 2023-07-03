class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        n = len(s)
        if(n < 10):
            return []
        
        s += '-'
        ans = set()
        counts = set()
        curr = deque(list(s[:10]))
        for c in s[10:]:
            joined = ''.join(curr)
            if(joined in counts):
                ans.add(joined)
            
            counts.add(joined)
            curr.popleft()
            curr.append(c)
        
        return ans
                
        