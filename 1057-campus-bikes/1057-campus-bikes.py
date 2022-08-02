class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        man_distance = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        heap = []
        combos = []
        for i,w in enumerate(workers):
            temp = sorted([(man_distance(w, b), i, j)\
                    for j, b in enumerate(bikes)], reverse=True)
            heap.append(temp.pop())
            combos.append(temp)
        
        heapify(heap)
        bikes_assigned = set()
        res = [-1] * len(workers)
        while(len(bikes_assigned) < len(workers)):
            _, w, b = heappop(heap)
            if(b not in bikes_assigned):
                bikes_assigned.add(b)
                res[w] = b
            else:
                heappush(heap, combos[w].pop())
        return res
            
                
            
                
        