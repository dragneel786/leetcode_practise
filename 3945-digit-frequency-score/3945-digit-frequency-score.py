class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = Counter()
        while(n > 0):
            mod = n % 10
            freq[mod] += 1
            n //= 10
        
        sums = 0
        for k, v in freq.items():
            sums += (k * v)
    
        return sums