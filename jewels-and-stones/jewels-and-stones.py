class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        uniq_jewels = set(jewels)
        count = 0
        for stone in stones:
            if(stone in uniq_jewels):
                count += 1
        
        return count