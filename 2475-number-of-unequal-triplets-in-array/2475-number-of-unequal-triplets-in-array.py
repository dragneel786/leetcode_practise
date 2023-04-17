class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        v = list(Counter(nums).values())
        counts = 0
        n = len(v)
        for i in range(n - 2):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    counts += (v[i] * v[j] * v[k])
        
        return counts
        