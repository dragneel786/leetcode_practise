class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [[max(0, i - a), i + a] for i, a \
                     in enumerate(ranges)]
        intervals.sort()
        
        taps = 0
        curr = 0 
        nxt = 0
        for start, end in intervals:
            if(nxt < start):
                return -1
                
            if(curr < start):
                curr = nxt
                taps += 1
            
            nxt = max(nxt, end)
            # print(curr, nxt)
            
        return taps + (nxt != curr and curr < n) if(nxt >= n) else -1