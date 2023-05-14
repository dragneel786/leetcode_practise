class Solution:
    def minNumberOfHours(self, ien: int, iex: int, en: List[int], ex: List[int]) -> int:
        
        tot_energy = 0
        thours = 0
        for i in range(len(en)):
            if(ex[i] >= iex):
                thours += (ex[i] + 1) - iex 
                iex += (ex[i] + 1) - iex 
            
            iex += ex[i]
            tot_energy += en[i]
        
        return thours + max(0, (tot_energy + 1) - ien)
    
        
        