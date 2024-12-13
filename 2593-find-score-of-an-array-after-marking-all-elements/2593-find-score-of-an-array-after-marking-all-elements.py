class Solution:
    def findScore(self, nums: List[int]) -> int:
        size = len(nums)
        marks = [True] * size
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)
        ret = 0
        while(heap):
            pop, i = heappop(heap)
            if marks[i]:
                ret += pop
                marks[i] = False
                if i - 1 > -1:
                    marks[i - 1] = False
                
                if i + 1 < size:
                    marks[i + 1] = False
                
        
        return ret