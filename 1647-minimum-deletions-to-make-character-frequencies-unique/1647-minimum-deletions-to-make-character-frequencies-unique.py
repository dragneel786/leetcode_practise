class Solution:
    def minDeletions(self, s: str) -> int:
        chars_map = Counter(s)
        appeared = set()
        deleted = 0
        for v in sorted(chars_map.values()):
            while(v in appeared):
                v -= 1
                deleted += 1
            
            if(v):
                appeared.add(v)
        
        return deleted
            
            