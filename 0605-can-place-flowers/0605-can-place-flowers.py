class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counts = 0
        fn = len(flowerbed)
        for i in range(fn):
            if(flowerbed[i] != 1 and\
               (i == 0 or not flowerbed[i - 1]) and\
               (i == fn - 1 or not flowerbed[i + 1])):
                counts += 1
                flowerbed[i] = 1
        
        return counts >= n
        
        
            
        