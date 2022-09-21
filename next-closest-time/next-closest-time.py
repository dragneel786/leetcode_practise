class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        def valid_format(val):
            ret = str(val)
            if(val < 10): return '0' + ret
            return ret
             
        
        def increment():
            nonlocal mm, hh
            temp_mm = int(mm) + 1
            
            if(temp_mm == 60):
                mm = str("00")
                hh = valid_format((int(hh) + 1) % 24)
            else:
                mm = valid_format(temp_mm)
    
        
        nums = set([c for c in time if(c != ':')])
        hh, mm = time.split(':')
        increment()
        
        while(hh + ':' + mm != time):
            for c in (hh+mm):
                if(c not in nums):
                    break
            else:
                return hh + ':' + mm
        
            increment()
        
        return time