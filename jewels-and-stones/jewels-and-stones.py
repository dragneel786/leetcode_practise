class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        uniq_jewels = set(jewels)
        return sum((1 for s in stones if(s in uniq_jewels)))