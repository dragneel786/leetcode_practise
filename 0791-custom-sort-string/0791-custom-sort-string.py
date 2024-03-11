class Solution:
    def customSortString(self, order: str, s: str) -> str:
        chars = Counter(s)
        ans = []
        for c in order:
            for _ in range(chars[c]):
                ans.append(c)
            
            del chars[c]
            
        for c, v in chars.items():
            for _ in range(v):
                ans.append(c)
        
        return ''.join(ans)