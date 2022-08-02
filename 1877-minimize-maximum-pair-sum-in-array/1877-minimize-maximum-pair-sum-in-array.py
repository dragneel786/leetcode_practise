class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        heap1, heap2 = nums[:], [-v for v in nums]
        heapify(heap1), heapify(heap2)
        ans = -inf
        for _ in range(len(nums) // 2):
            ans = max(ans, heappop(heap1) - heappop(heap2))
        return ans