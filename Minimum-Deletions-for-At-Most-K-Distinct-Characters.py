class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        values = [v for v in Counter(s).values()]
        values.sort()
        diff = len(values) - k
        if diff < 0:
            return 0
        
        return sum(values[:diff])