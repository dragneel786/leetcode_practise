class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        imap = defaultdict(list)
        for i, num in enumerate(nums):
            imap[num].append(i)
        
        res = 0
        for idxs in imap.values():
            for a, b in combinations(idxs, 2):
                res += (a * b) % k == 0
                
        return res