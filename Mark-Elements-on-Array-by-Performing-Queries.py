class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]
        tot = sum(nums)
        heapify(heap)

        res = []
        for i, k in queries:
            tot -= nums[i]
            nums[i] = 0
            while(heap and k):
                val, index = heappop(heap)
                if val == nums[index]:
                    tot -= val
                    nums[index] = 0
                    k -= 1
            
            res.append(tot)

        return res
