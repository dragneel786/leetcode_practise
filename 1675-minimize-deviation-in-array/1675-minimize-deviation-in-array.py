from sortedcontainers import SortedSet
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        scontain = SortedSet()
        for num in nums:
            if(num % 2):
                num *= 2
            scontain.add(num)
    
        ans = inf
        while(True):
            max_val = scontain.pop()
            min_val = scontain.pop(0) if(scontain) else max_val
            ans = min(max_val - min_val, ans)
            if(max_val % 2 == 1):
                break
            
            scontain.add(max_val // 2)
            scontain.add(min_val)
        
        return ans