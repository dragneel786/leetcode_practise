class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(lambda:0)
        for n in nums:
            counter[n] += 1
        
        h = []
        for ke in counter.keys():
            heappush(h, (counter[ke], ke))
            if(len(h) > k):
                heappop(h)
         
        res = []
        for v in h:
            res.append(v[1])
        
        return res