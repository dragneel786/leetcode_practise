class Solution:
    def maxSum(self, nums: List[int]) -> int:
        pairs = defaultdict(list)
        for num in nums:
            max_v = 0
            temp = num
            while(num):
                max_v = max(max_v, num % 10)
                num //= 10
            pairs[max_v].append(temp)
        
        ans = -1
        for values in pairs.values():
            if(len(values) > 1):
                a, b = sorted(values)[-2:]
                ans = max(ans, a + b)
        
        return ans
        