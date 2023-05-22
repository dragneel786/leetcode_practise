class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(10 ** 4)]
        for v, c in Counter(nums).items():
            bucket[c].append(v)
        
        ans = []
        for i in range(10 ** 4 - 1, -1, -1):
            for v in bucket[i]:
                ans.append(v)
                
                if(len(ans) == k):
                    return ans
        
        return ans
        