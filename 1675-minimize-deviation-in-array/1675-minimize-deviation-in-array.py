class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        q = []
        minV = float('inf')
        for i in range(len(nums)):
            if(nums[i] & 1):
                nums[i] *= 2
            minV = min(minV,  nums[i])
            heapq.heappush(q, -1 * nums[i])

        dev = float('inf')
        while(not q[0] % 2):
            val = -1 * q[0]
            dev = min(dev, val - minV)
            heapq.heappop(q)
            minV = min(minV, val // 2)
            heapq.heappush(q, -1 * val // 2)
        
        return min(dev, (-1 * q[0]) - minV)