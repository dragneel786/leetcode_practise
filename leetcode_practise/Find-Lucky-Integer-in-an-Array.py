class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnts = Counter(arr)
        ans = -1
        for k, v in cnts.items():
            if k == v:
                ans = max(ans, k)
        
        return ans
        