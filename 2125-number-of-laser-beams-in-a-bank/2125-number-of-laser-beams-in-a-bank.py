class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        for b in bank:
            counts = b.count('1')
            ans += prev * counts
            if(counts):
                prev = counts
        
        return ans