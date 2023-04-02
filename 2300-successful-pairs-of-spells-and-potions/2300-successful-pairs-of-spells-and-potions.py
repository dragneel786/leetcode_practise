class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        def bin_search(s):
            nonlocal success, n
            low = 0
            high = n
            while(low < high):
                mid = (high - low) // 2 + low
                if(potions[mid] * s < success): low = mid + 1
                else:
                    high = mid
            
            return low
        
        m, n = len(spells), len(potions)
        potions.sort()
        ans = []
        for s in spells:
            ans.append(n - bin_search(s))
        
        return ans
        
            