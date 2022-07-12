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
        
        @lru_cache(None)
        def makeIt(i, form):
            nonlocal posSide
            if(i == n):
                if(sides[0] == sides[1] == sides[2] == sides[3]):
                    return True
                return False

            for j in range(4):
                if(sides[j] + matchsticks[i] > posSide):
                    continue
                 
                sides[j] += matchsticks[i]
                if(makeIt(i + 1, getForm())):
                    return True
                sides[j] -= matchsticks[i]
                
            return False
        
        sides = [0,0,0,0]
        posSide = perimeter // 4
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        return makeIt(0, getForm)