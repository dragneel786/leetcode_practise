class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1 = [nums[0]]
        a2 = [nums[1]]
        for v in nums[2:]:
            if(a1[-1] > a2[-1]):
                a1.append(v)
            
            else:
                a2.append(v)
        
        return a1 + a2