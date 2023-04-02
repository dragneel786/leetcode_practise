class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        spell_index = [(s, i) for i, s in enumerate(spells)]
        spells.clear()
        
        spell_index.sort()
        potions.sort()
        ans = [0] * len(spell_index)
        n = len(potions)

        potion_index = len(potions) - 1
        for spell, index in spell_index:
            while(potion_index >= 0 and \
                    (spell * potions[potion_index]) >= success):

                potion_index -= 1
                
            ans[index] = (n - potion_index - 1)
        
        return ans
            
            