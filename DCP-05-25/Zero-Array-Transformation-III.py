class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        queries.sort()
        diff = [0] * (n + 1)
        
        heap = []
        ops = idx = 0
        for i, num in enumerate(nums):
            ops += diff[i]
            while(idx < len(queries) and queries[idx][0] == i):
                heappush(heap, -queries[idx][1])
                idx += 1
            
            while(ops < num and heap and -heap[0] >= i):
                diff[-heappop(heap) + 1] -= 1
                ops += 1
            
            if ops < num:
                return -1
        
        return len(heap)

