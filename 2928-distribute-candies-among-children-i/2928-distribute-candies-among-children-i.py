class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for a in range(limit + 1):
            for b in range(limit + 1):
                for c in range(limit + 1):
                    if(a + b + c == n):
                        count += 1
        
        return count
            
            