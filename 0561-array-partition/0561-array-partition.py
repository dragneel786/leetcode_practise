class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        num_counts = [0] * (20_001)
        for num in nums:
            num_counts[num + 10_000] += 1
        
        odd = True
        ans = 0
        for i in range(20_001):
            while(num_counts[i]):
                if(odd):
                    ans += (i - 10_000)
                odd = not odd
                num_counts[i] -= 1
        
        return ans
                
            