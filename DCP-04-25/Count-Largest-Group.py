class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = Counter()
        max_val = max_tot = 0
        for v in range(1, n + 1):
            s = 0
            while(v): 
                s += v % 10
                v //= 10
            
            counts[s] += 1
            if max_val < counts[s]:
                max_val = counts[s]
                max_tot = 0
            
            max_tot += counts[s] == max_val
        
        return max_tot

