class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_counts = Counter(nums)
        ans = 0
        for v in num_counts.values():
            if(v == 1):
                return -1
            
            div = v // 3
            if(v % 3 == 2 or v % 3 == 1):
                ans += div + 1
            
            else:
                ans += div
        
        return ans
        
            