class Solution:
    def findLucky(self, arr: List[int]) -> int:
        acount = Counter(arr)
        ans = -1
        for a, v in acount.items():
            if(a == v and a > ans):
                ans = a
        
        return ans
        