class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if(buckets == 1):
            return 0
        
        buckets -= 1
        base = (minutesToTest // minutesToDie) + 1
        print(base)
        res = 0
        while(buckets > 0):
            buckets //= base
            res += 1
        return res