class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = []
        end = []
        for s, e in flowers:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()
        
        res = []
        for p in people:
            started = bisect_right(start, p)
            ended = bisect_left(end, p)
            res.append(started - ended)
        
        return res
            
        
        