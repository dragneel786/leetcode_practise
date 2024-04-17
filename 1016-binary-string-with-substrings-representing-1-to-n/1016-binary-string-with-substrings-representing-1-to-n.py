class Solution:
    def queryString(self, s: str, n: int) -> bool:
        num_set = set()
        for start in range(len(s)):
            for end in range(start, len(s)):
                num_set.add(int(s[start: end + 1], 2))
        
        
        for num in range(1, n + 1):
            if num not in num_set:
                return False
        
        return True