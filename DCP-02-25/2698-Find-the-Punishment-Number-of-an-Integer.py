class Solution:
    def punishmentNumber(self, n: int) -> int:
        def is_pun(val, curr = 0):
            nonlocal v
            if not val:
                return curr == v

            for j in range(1, len(val) + 1):
                if is_pun(val[j:], curr + int(val[:j])):
                    return True
            
            return False

        tot = 1
        for v in range(9, n + 1):
            tot += (v * v) if is_pun(str(v * v)) else 0
        
        return tot