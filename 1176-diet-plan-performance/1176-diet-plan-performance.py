class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        tot = sum(calories[:k])
        calories.append(10)
        points = 0
        for i in range(k, len(calories)):
            if(tot < lower):
                points -= 1

            elif(tot > upper):
                points += 1
            
            tot += calories[i]
            if(i - k > -1):
                tot -= calories[i - k]
            
        return points
        
        