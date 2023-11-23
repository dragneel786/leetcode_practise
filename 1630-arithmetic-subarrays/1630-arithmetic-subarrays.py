class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def check_arithmetic(li):
            li.sort()
            for i in range(1, len(li) - 1):
                if(li[i] - li[i - 1] != li[i + 1] - li[i]):
                    return False
            
            return True
                
        
        ans = []
        for start, end in zip(l, r):
            ans.append(check_arithmetic(nums[start: end + 1]))
        
        return ans
            