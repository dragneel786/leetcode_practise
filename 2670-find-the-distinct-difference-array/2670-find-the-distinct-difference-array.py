class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        dis_arr = []
        prefix = Counter()
        suffix = Counter(nums)
        for num in nums:
            prefix[num] += 1
            suffix[num] -= 1
            if(not suffix[num]):
                del suffix[num]
            
            dis_arr.append(len(prefix) - len(suffix))
        
        return dis_arr
            