class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        n += 1
        in_order = Counter()
        out_order = {i:[] for i in range(n)}
        for a, b in relations:
            in_order[b] += 1
            out_order[a].append(b)
        
        heap = []
        for c in range(1, n):
            if(in_order[c] == 0):
                heap.append((time[c - 1], c))
        heapify(heap)
        
        res = 0
        while(heap):
            t, course = heappop(heap)
            for c in out_order[course]:
                in_order[c] -= 1
                if(in_order[c] == 0):
                    heappush(heap, (t + time[c - 1], c))
        
            res = t
        
        return res
            
        
        
        
        