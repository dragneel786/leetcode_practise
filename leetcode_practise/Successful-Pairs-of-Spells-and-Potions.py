class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        def find_pos(val):
            low, high = 0, size
            index = size
            while(low < high):
                mid = low + ((high - low) // 2)
                if potions[mid] * val >= success:
                    index = mid
                    high = mid
                else:
                    low = mid + 1
            
            return index

        ans = []
        size = len(potions)
        potions.sort()
        for sp in spells:
            index = find_pos(sp)
            ans.append(size - index)
        
        return ans


        

        