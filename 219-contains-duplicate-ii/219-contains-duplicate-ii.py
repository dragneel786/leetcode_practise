class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(lambda:[])
        for i in range(len(nums)):
            for v in seen[nums[i]]:
                if(abs(v - i) <= k):
                    return True
            seen[nums[i]].append(i)
        
        return False