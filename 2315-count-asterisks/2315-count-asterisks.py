class Solution:
    def countAsterisks(self, s: str) -> int:
        
        values = s.split('|')
        ans = values[0].count("*")
        for i in range(2, len(values), 2):
            print(values[i])
            ans += values[i].count("*")
        
        return ans
            