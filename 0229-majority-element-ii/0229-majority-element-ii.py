class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        n = len(nums)
        cmap = Counter()
        for num in nums:
            cmap[num] += 1
            if(cmap[num] > (n // 3)):
                res.add(num)
        
        return res