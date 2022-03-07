class Solution:
    def average(self, nums: List[int]) -> float:
        minV, maxV, sumV = float('inf'), 0, 0
        for n in nums:
            if(n > maxV):
                maxV = n
            
            if(n < minV):
                minV = n
            
            sumV += n
        
        return (sumV - minV - maxV) / (len(nums) - 2)
        