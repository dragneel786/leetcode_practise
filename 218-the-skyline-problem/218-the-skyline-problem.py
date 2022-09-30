class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def seperate_start_end():
            seperated = []
            for start, end, height in buildings:
                seperated.append([start, -height])
                seperated.append([end, height])
            
            seperated.sort()
            return seperated
        
        points = seperate_start_end()
        heap = [0]
        curr = 0
        res = []

        for x, height in points:
            if(height < 0):
                if(-height > curr):
                    res.append([x, -height])
                    curr = -height

                heappush(heap, height)
            else:
                heap.remove(-height)
                heapify(heap)
                if(curr != -heap[0]):
                    curr = -heap[0]
                    res.append([x, -heap[0]])
        
        return res