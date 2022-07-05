class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i = j = 0
        m, n = len(slots1), len(slots2)
        while(i < m and j < n):
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            s, e = max(s1, s2), min(e1, e2)
            if(s + duration <= e):
                return [s, s + duration]
            if(e1 > e2): j += 1
            else: i += 1
        return []
            
            
        