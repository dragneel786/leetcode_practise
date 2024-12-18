class Solution:
    def maxProduct(self, s: str) -> int:
        
        @lru_cache(None)
        def get_len(i, p1 = "", p2 = ""):
            if i >= len(s):
                if p1[::-1] == p1 and p2[::-1] == p2:
                    return len(p1) * len(p2)
                
                return 0
            
            
            return max(get_len(i + 1, p1 + s[i], p2),\
                       get_len(i + 1, p1, p2 + s[i]),\
                       get_len(i + 1, p1, p2))
            
        return get_len(0)