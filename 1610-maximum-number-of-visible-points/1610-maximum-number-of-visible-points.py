class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        radians, same = [], 0
        x, y = location
        
        for px, py in points:
            if(x == px and y == py):
                same += 1
                continue
            radians.append(math.atan2(py - y, px - x))
        
        radians.sort()
        radians = radians + [r + 2.0 * math.pi for r in radians]
        angle = math.pi * angle / 180
        
        ans = l = 0
        for r in range(len(radians)):
            while(radians[r] - radians[l] > angle):
                l += 1
            ans = max(r - l + 1, ans)
            
        return ans + same