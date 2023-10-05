class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = 0, 1
        cnt1 = cnt2 = 0
        for num in nums:
            if(cand1 == num):
                cnt1 += 1
            
            elif(cand2 == num):
                cnt2 += 1
            
            elif(cnt1 == 0):
                cand1, cnt1 = num, 1
            
            elif(cnt2 == 0):
                cand2, cnt2 = num, 1
            
            else:
                cnt1, cnt2 = cnt1 - 1, cnt2 - 1
        
        return [num for num in (cand1, cand2) \
               if nums.count(num) > (len(nums) // 3)]
            
        