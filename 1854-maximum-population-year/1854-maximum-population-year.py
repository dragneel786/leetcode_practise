class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101
        for l in logs:
            b, d = l[0] - 1950, l[1] - 1950
            years[b] += 1
            years[d] -= 1
        
        maxCount = years[0]
        maxYear = 1950
        for i in range(1, 101):
            years[i] += years[i - 1]
            if(years[i] > maxCount):
                maxCount = years[i]
                maxYear = 1950 + i
        
        return maxYear