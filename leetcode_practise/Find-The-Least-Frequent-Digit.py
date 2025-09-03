class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        counts = Counter()
        while(n):
            counts[n % 10] += 1
            n //= 10

        ans, min_count = 0, inf
        for num, count in counts.items():
            if count < min_count:
                ans = num
                min_count = count
            
            elif count == min_count:
                ans = min(ans, num)

        return ans
        