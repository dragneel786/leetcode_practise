class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem_count = Counter()
        ans = 0
        for t in time:
            val = t % 60
            ans += rem_count[60 - (val if(val) else 60)]
            rem_count[val] += 1
        
        return ans