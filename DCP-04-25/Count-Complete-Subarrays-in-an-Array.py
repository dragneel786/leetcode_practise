class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counts = Counter()
        n, right, res = len(nums), 0, 0
        uniq_counts = len(set(nums))
        for left, num in enumerate(nums):
            if left > 0:
                counts[nums[left - 1]] -= 1
                if counts[nums[left - 1]] == 0:
                    del counts[nums[left - 1]]
            
            while(right < n and len(counts) < uniq_counts):
                counts[nums[right]] += 1
                right += 1
            
            if len(counts) == uniq_counts:
                res += n - right + 1
        
        return res
            
        
                    
            
                
                
            