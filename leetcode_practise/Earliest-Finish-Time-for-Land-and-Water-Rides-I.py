class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        earliest = inf
        for l, ld in zip(landStartTime, landDuration):
            for w, wd in zip(waterStartTime, waterDuration):
                mn_s, mn_d = l, ld
                mx_s, mx_d = w, wd
                if w < l:
                    mn_s, mx_s = mx_s, mn_s
                    mn_d, mx_d = mx_d, mn_d
                
                first_end = mn_s + mn_d
                earliest = min(earliest, max(first_end, mx_s) + mx_d)
        
        return earliest
                

