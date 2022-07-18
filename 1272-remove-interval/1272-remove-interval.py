class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for low, high in intervals:
            rlow, rhigh = toBeRemoved
            if(high <= rlow or low >= rhigh):
                res.append([low, high])
            else:
                if(low < rlow):
                    res.append([low, rlow])
                if(high > rhigh):
                    res.append([rhigh, high])
        return res