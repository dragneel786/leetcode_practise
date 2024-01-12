class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        tot = k = 0
        n = len(grades)
        while(tot + k + 1 <= n):
            k += 1
            tot += k
        
        return k