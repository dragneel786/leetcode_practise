class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = Counter(s)
        vfeq = cfeq = 0
        for k, v in counts.items():
            if k in 'aeiou':
                vfeq = max(vfeq, v)
            else:
                cfeq = max(cfeq, v)
            
        return vfeq + cfeq