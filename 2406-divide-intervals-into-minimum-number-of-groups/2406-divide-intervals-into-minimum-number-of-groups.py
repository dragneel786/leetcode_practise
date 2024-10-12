class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for s, e in intervals:
            if heap and heap[0] < s:
                heappop(heap)
                
            heappush(heap, e)
            # print(heap, s, e)
        return len(heap)
                
            