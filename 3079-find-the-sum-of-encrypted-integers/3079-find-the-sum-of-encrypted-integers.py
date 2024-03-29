class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            max_val = count = 0
            str_num = str(num)
            while(num):
                count += 1
                max_val = max(max_val, num % 10)
                num //= 10
            
            ans += int(len(str_num) * str(max_val))
        
        return ans
            
            
                
            