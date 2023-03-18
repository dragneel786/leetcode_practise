class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sc = Counter(s)
        ans = inf
        for k, v in Counter(target).items():
            if((sc[k] // v) == 0):
                return 0
            
            ans = min(ans, sc[k] // v)
        
        return ans if(ans != inf) else 0