class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        hash_it = Counter()
        pairs = 0
        MOD = (10 ** 9) + 7
        for num in nums:
            val = num - int(str(num)[::-1])
            pairs = (pairs + hash_it[val]) %  MOD
            hash_it[val] += 1
        
        return pairs
            
            
        