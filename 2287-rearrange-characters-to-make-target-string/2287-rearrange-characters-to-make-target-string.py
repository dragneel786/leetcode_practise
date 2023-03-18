class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sc = Counter(s)
        ans = inf
        for k, v in Counter(target).items():
            ans = min(ans, sc[k] // v)
        
        return ans