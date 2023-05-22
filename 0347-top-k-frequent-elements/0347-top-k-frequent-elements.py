class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ks = []
        li = [0] * 20001
        for num in nums:
            idx = num + 10000
            li[idx] += 1
        
        for i in range(20001):
            if(li[i] > 0):
                insort(ks, (-li[i], i - 10000))
            
            if(len(ks) > k):
                ks.pop()
        
        return [v[1] for v in ks]