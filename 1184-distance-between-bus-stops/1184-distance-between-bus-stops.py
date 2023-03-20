class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        d1 = d2 = start
        ans1 = ans2 = 0
        while(d1 != destination):
            ans1 += distance[d1]
            d1 = (d1 + 1) % n
        
        while(d2 != destination):
            d2 = d2 - 1 if(d2) else n - 1
            ans2 += distance[d2]
        
        return min(ans1, ans2)