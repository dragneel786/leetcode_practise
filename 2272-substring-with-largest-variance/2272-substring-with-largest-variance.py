class Solution:
    def largestVariance(self, s: str) -> int:
        counts = Counter(s)
        ans = 0
        for a, b in permutations(counts, 2):
            seen_a = seen_b = False
            c1 = counts[a]
            c2 = counts[b]
            diff = 0
            for c in s:
                if(diff < 0):
                    if not c1:
                        break
                        
                    if not c2:
                        ans = max(ans, diff + c1)
                        break
                    
                    seen_a = seen_b = False
                    diff = 0
                    
                if(c == a):
                    c1 -= 1
                    diff += 1
                    seen_a = True

                if(c == b):
                    c2 -= 1
                    diff -= 1
                    seen_b = True
                
                if(seen_a and seen_b):
                    ans = max(diff, ans)
        
        return ans