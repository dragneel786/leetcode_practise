class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def returnCost(n, s):
            cost = 0
            for c in n:
                if(c == s):
                    cost += pushCost
                else:
                    cost += (moveCost + pushCost)
                    s = c
            return cost
        
        def mmCost(n):
            if(not n):
                return 0
            return returnCost(str(n), str(startAt))
        
        def ssCost(n, s):
            n = str(n)
            if(0 <= int(n) < 10):
                n = "0" + n
            return returnCost(n, s)
            
        if(targetSeconds < 10):
            return pushCost if targetSeconds == startAt else (moveCost + pushCost)
        
        minCost = math.inf
        for i in range(100):
            mint, sec = i, targetSeconds - (i * 60)
            if(i == 99):
                pass
            if((mint * 60) <= targetSeconds and 0 <= sec < 100):
                print(f'{mint}:{sec}')
                costM = mmCost(mint)
                if(costM):
                    costM += ssCost(sec, str(i % 10))
                else:
                    costM += ssCost(sec, str(startAt))
                minCost = min(costM, minCost)
                
        return minCost
        
            