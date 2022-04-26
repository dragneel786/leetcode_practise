class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(lambda:[])
        n = len(nums)
        for i in range(n):
            seen[nums[i]].append(i)
        
        for v in seen.keys():
            ind = seen[v]
            print(ind)
            for i in range(len(ind)):
                for j in range(i + 1, len(ind)):
                    if(abs(ind[i] - ind[j]) <= k):
                        return True
        
        return False