class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        def brute_it(size):
            counts = Counter()
            max_ret = 0
            for i in range(len(s) - size + 1):
                sslice = s[i: i + size]
                if len(Counter(sslice)) <= maxLetters:
                    counts[sslice] += 1
                    max_ret = max(max_ret, counts[sslice])
                    
            return max_ret
        
        res = 0
        for size in range(minSize, maxSize + 1):
            res = max(res, brute_it(size))
        
        return res
        