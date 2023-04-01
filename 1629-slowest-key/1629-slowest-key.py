class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        key = keysPressed[0]
        prevl = lag = releaseTimes[0]
        for k, r in zip(keysPressed[1:], releaseTimes[1:]):
            cd = r - prevl
            print(cd)
            if(cd > lag or lag == cd):
                key = max(k, key) if(lag == cd) else k
                lag = cd
            
            prevl = r
            
        return key
                