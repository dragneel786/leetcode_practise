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

        return (values * 2) + odds >= k
        