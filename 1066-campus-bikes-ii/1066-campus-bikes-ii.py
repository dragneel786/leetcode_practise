class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        manhattan_dist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        xor = lambda w, t: w ^ (1 << t)
        
        def getMinDist(worker_idx, b_masks, memo = {}):
            nonlocal n
            key = (worker_idx, b_masks)
            
            if(worker_idx >= n):
                return 0
        
            if(key in memo):
                return memo[key]
            
            min_dist = inf
            for j, b in enumerate(bikes):
                if(b_masks & (1 << j)):
                    val = manhattan_dist(workers[worker_idx], b)
                    min_dist = min(min_dist, getMinDist(worker_idx + 1, xor(b_masks, j)) + val)
            
            memo[key] = min_dist
            return min_dist
        
        n = len(workers)
        m = len(bikes)
        return getMinDist(0, (1 << m) - 1)