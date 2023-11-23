class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def check_arithmetic(li):
            min_e = min(li)
            max_e = max(li)
            val_diff = (max_e - min_e)
            if(val_diff % (len(li) - 1) != 0):
                return False
            
            
            diff = val_diff / (len(li) - 1)
            li = set(li)
            e = min_e
            while(e < max_e):
                if(e not in li):
                    return False
                
                e += diff
            
            return True
        
        
        ans = []
        for start, end in zip(l, r):
            ans.append(check_arithmetic(\
                nums[start: end + 1]))
        
        return ans
            