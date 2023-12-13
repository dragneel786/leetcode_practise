class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        count = idx = 0
        for num in nums:
            if(prev == num):
                count += 1
                continue
            
            for _ in range(min(count, 2)):
                nums[idx] = prev
                idx += 1
            
            count = 1
            prev = num
        
        for _ in range(min(count, 2)):
            nums[idx] = prev
            idx += 1
        
        return idx
            
            
            
                    