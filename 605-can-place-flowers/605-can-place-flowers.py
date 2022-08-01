class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        nxt = prev = 0
        l = len(flowerbed)
        count = 0
        for i, f in enumerate(flowerbed):
            if(not f):
                nxt = 1 if(i == l - 1 or not flowerbed[i + 1]) else 0
                prev = 1 if(i == 0 or not flowerbed[i - 1]) else 0
                if(nxt and prev):
                    flowerbed[i] = 1
                    count += 1
        
        return count >= n
                
            
        
        
            
            
            
            