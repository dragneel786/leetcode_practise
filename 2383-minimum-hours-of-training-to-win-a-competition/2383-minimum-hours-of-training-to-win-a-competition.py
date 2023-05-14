class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
        tot_energy = sum(energy)
        curr_exp = initialExperience
        thours = 0
        for e in experience:
            if(e >= curr_exp):
                thours += (e + 1) - curr_exp 
                curr_exp += (e + 1) - curr_exp 
            curr_exp += e
        
        return thours + max(0, (tot_energy + 1) - initialEnergy)
    
        
        