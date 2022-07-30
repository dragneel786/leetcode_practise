class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        manhattan_dist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        xor = lambda w, t: w ^ (1 << t)
        
        @lru_cache(None)
        def getMinDist(worker_idx, b_masks, dist = 0):
            nonlocal minSoFar, n
            
            if(worker_idx >= n):
                minSoFar = min(dist, minSoFar)
                return
            
            if(dist >= minSoFar):
                return
            
            for j, b in enumerate(bikes):
                if(b_masks & (1 << j)):
                    val = manhattan_dist(workers[worker_idx], b)
                    getMinDist(worker_idx + 1, xor(b_masks, j), dist + val)
        
        
        n = len(workers)
        m = len(bikes)
        minSoFar = inf
        getMinDist(0, (1 << m) - 1)
        return minSoFar