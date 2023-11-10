class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        path = defaultdict(list)
        for a, b in adjacentPairs:
            path[a].append(b)
            path[b].append(a)
        
        start = None
        end = None
        for k in path.keys():
            if(len(path[k]) == 1):
                if(start is None): 
                    start = k
                else:
                    end = k
          
        stored = set([start])
        res = [start]
        start = path[start][0]
        for _ in range(len(adjacentPairs) - 1):
            res.append(start)
            stored.add(start)
            a, b = path[start]
            if(a in stored):
                start = b
            else:
                start = a
        
        res.append(end)
        return res
                
        
        
        
        