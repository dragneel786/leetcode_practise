class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        ans = ''
        for c, v in sorted([(v, c) for c, v in counts.items()], reverse=True):
            ans += (c * v)
        
        return ans
            