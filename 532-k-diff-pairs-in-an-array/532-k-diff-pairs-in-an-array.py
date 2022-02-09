class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        for n in nums:
            seen[n] += 1
        count = 0
        for n in list(seen.keys()):
            if(k == 0):
                count += 1 if(seen[n] > 1) else 0
            else:
                count += 1 if(seen[n + k]) else 0

        return count