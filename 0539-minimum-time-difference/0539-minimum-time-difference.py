class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_in_mins(time):
            hours, mins = time.split(":")
            return int(hours) * 60 + int(mins)
        
        mints = []
        for tp in timePoints:
            mints.append(convert_in_mins(tp))
        
        
        res = inf
        mints.sort()
        size = len(mints)
        for i in range(len(mints)):
            mn_time, mx_time = min(mints[i], mints[i - 1]),\
            max(mints[i], mints[i - 1])
            res = min(res, (1440 - mx_time) + mn_time,\
                      mx_time - mn_time)
            
            
            mn_time, mx_time = min(mints[i], mints[(i + 1) % size]),\
            max(mints[i], mints[(i + 1) % size])
            res = min(res, (1440 - mx_time) + mn_time,\
                      mx_time - mn_time)
            
        return res