class Solution:
    def minimumDeletions(self, s: str) -> int:
        bs_count = 0
        min_dp = [0]
        for c in s:
            if c == "b":
                bs_count += 1
                min_dp.append(min_dp[-1])
            else:
                min_dp.append(min(min_dp[-1] + 1, bs_count))
            
            # print(c, min_dp)
            
        return min_dp[-1]
            
        
        