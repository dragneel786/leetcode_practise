class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapi = {0:-1}
        max_len = count = 0
        for i in range(len(nums)):
            count += 1 if(nums[i]) else -1
            if(count in mapi):
                max_len = max(max_len, i - mapi.get(count))
            else:
                mapi[count] = i
        
        return max_len