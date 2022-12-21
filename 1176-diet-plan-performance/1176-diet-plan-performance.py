class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        tot = 0
        points = 0
        for i in range(len(calories)):
            tot += calories[i]
            if(i >= k - 1):
                if(i - k >= 0):
                    tot -= calories[i - k]
            
                if(tot < lower):
                    points -= 1

                elif(tot > upper):
                    points += 1
            
        return points
        
        