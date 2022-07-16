class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if(n % k != 0):
            return False
        
        counts = Counter(nums)
        nums.sort()
        for i,v in enumerate(nums):
            if(counts[v]):
                start, r = v, 0
                while(counts[start] and r < k):
                    counts[start] -= 1
                    start += 1
                    r += 1
                if(r != k):
                    return False
        
        return True
            