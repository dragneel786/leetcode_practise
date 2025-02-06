class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counts = Counter()
        for i, a in enumerate(nums):
            for b in nums[i + 1:]:
                counts[a * b] += 1
        
        print(counts)
        res = 0
        for v in counts.values():
            pairs_of_equal_product = (v - 1) * v // 2
            res += 8 * pairs_of_equal_product
        
        return res