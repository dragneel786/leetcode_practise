class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        heap = []
        
        for num in set(nums):
            if(len(heap) < 3 or heap[0] < num):
                heappush(heap, num)
            
            if(len(heap) > 3):
                heappop(heap)
        
        
        return heap[0] if(len(heap) >= 3) else heap[-1]