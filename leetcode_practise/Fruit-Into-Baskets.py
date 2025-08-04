class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = Counter()
        ans = tot = start = 0
        for end, f in enumerate(fruits):
            counts[f] += 1
            while(len(counts) > 2):
                counts[fruits[start]] -= 1
                if counts[fruits[start]] == 0:
                    del counts[fruits[start]]

                start += 1
            
            ans = max(ans, end - start + 1)
        
        return ans

            

        

                
            