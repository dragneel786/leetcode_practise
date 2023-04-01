class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key = chr(ord('a') - 1)
        lag = 0
        prevl = 0
        for k, r in zip(keysPressed, releaseTimes):
            cd = r - prevl
            if(cd > lag):
                lag = cd
                key = k
            
            if(cd == lag):
                key = max(k, key)
            
            prevl = r
    
        return key
                