class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        man_distance = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        combos = []
        for i,w in enumerate(workers):
            for j,b in enumerate(bikes):
                combos.append((man_distance(w, b), i, j))
                
        combos.sort()
        bikes_assigned = set()
        workers_assigned = set()
        res = [0] * len(workers)
        for c in combos:
            _, w, b = c
            if(w not in workers_assigned and\
              b not in bikes_assigned):
                res[w] = b
                workers_assigned.add(w)
                bikes_assigned.add(b)
        
        return res