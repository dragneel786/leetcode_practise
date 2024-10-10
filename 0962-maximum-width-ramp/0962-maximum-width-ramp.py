class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        st = []
        max_ramp = 0
        for j, num in enumerate(nums):
            if not st or num < st[-1][1]:
                st.append((j, num))
            
            else:
                for i, v in st[::-1]:
                    if v > num:
                        break
                    # print(j, i, (j - i))   
                    max_ramp = max(max_ramp, (j - i))
        
        return max_ramp