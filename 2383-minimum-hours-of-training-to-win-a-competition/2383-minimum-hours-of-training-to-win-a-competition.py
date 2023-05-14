class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
        tot_energy = 0
        curr_exp = initialExperience
        thours = 0
        for i in range(len(energy)):
            e = experience[i]
            if(e >= curr_exp):
                thours += (e + 1) - curr_exp 
                curr_exp += (e + 1) - curr_exp 
            
            curr_exp += e
            tot_energy += energy[i]
        
        return thours + max(0, (tot_energy + 1) - initialEnergy)
    
        
        