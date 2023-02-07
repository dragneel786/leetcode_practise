class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fmax = [-1, 0]
        smax = [-1, 0]
        curr = [-1, 0]
        fruits.append(inf)
        max_ans = 0
        for i, fru in enumerate(fruits):
            if(fmax[0] == fru):
                fmax[0] = fru
                fmax[1] += 1
            
            elif(smax[0] == fru):
                smax[0] = fru
                smax[1] += 1
            
            else:
                max_ans = max(max_ans, smax[1] + fmax[1])
                fmax = curr
                smax = [fru, 1]
            
            if(curr[0] != fru):
                curr = [fru, 0]
            
            curr[1] += 1
            
        return max_ans
                
        
        