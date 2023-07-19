class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        counts = 0
        for a, b in combinations(nums, 2):
            counts += gcd(int(str(a)[0]), int(str(b)[-1])) == 1
        return counts