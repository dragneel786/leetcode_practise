class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for v, c in counter.items():
            bucket[c].append(v)
        
        ans = []
        for i in range(len(nums), -1, -1):
            for v in bucket[i]:
                ans.append(v)
                
                if(len(ans) == k):
                    return ans
        
        return ans
        