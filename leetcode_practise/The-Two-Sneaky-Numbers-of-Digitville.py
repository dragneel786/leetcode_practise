class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []
        for k, v in counts.items():
            if v == 2:
                res.append(k)
        
        return res