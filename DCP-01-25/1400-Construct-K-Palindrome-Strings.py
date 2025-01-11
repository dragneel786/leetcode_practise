class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        values = odds = 0
        print(Counter(s))
        for v in Counter(s).values():
            if v % 2 == 1:
                odds += 1
            
            values += (v // 2)

        if odds > k:
            return False
        
        for v in range(values + 1):
            # print(((values - v), (v * 2), odds))
            if ((values - v) + (v * 2) + odds) >= k:
                return True

        return False
        