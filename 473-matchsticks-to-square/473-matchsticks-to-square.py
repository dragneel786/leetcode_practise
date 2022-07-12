class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if(perimeter % 4 != 0):
            return False

        def getForm():
            res = ""
            for s in sides:
                res += str(s)
            return res
        
        def makeIt(i, form):
            nonlocal posSide
            key = (i, form)
            if(i == n):
                if(sides[0] == sides[1] == sides[2] == sides[3]):
                    return True
                return False
            
            if(key in memo):
                return memo[key]
            
            res = False
            for j in range(4):
                if(sides[j] + matchsticks[i] > posSide):
                    continue
                 
                sides[j] += matchsticks[i]
                if(makeIt(i + 1, getForm())):
                    res = True
                    break
                    
                sides[j] -= matchsticks[i]
            
            memo[key] = False
            return res
        
        sides = [0,0,0,0]
        posSide = perimeter // 4
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        memo = {}
        return makeIt(0, getForm)