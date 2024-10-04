class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        start = chemistry = 0
        end = n - 1
        curr_sum = skill[0] + skill[-1]
        while(start < end):
            if curr_sum != (skill[start] + skill[end]):
                return -1
            
            chemistry += (skill[start] * skill[end])
            start += 1
            end -= 1
        
        return chemistry
            
            