class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def get_sum(counts):
            heap = []
            for k, v in counts.items():
                heappush(heap, [-v, -k])
            
            ans = 0
            for _ in range(min(x, len(heap))):
                k, v = heappop(heap)
                ans += (-v * -k)
            
            return ans

        res = []
        counts = Counter()
        for i, num in enumerate(nums):
            counts[num] += 1
            if i >= k - 1:
                if i >= k:
                    counts[nums[i - k]] -= 1
                res.append(get_sum(counts))
        
        return res
        

