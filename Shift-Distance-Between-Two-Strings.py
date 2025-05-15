class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        for i in range(1, 26):
            nextCost[i] += nextCost[i - 1]
            previousCost[i] += previousCost[i - 1]
        
        tot = 0
        print("P", previousCost)
        print("N", nextCost)
        for charc, chart in zip(s, t):
            cost = 0
            cidx, tidx = ord(charc) - 97, ord(chart) - 97
            if cidx < tidx:
                ncost = nextCost[tidx - 1]
                if cidx > 0:
                    ncost -= nextCost[cidx - 1]
                
                pcost = previousCost[cidx]
                if tidx < 25:
                    pcost += previousCost[25] - previousCost[tidx]
                
                cost = min(ncost, pcost)
                # print(ncost, pcost)
            
            elif cidx > tidx:
                ncost = nextCost[25] - nextCost[cidx - 1]
                if tidx > 0:
                    ncost += nextCost[tidx - 1]
                
                pcost = previousCost[cidx] - previousCost[tidx]
                
                cost += min(ncost, pcost)
                # print(ncost, pcost)
            
            tot += cost
            
        return tot
        
        