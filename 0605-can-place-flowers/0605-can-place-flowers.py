class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower_index = [inf] * len(flowerbed)
        idx = inf
        for i in range(len(flowerbed) - 1, -1, -1):
            if flowerbed[i] == 1:
                idx = i
            flower_index[i] = idx
        
        planted = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            
            # print((i == 0 or flowerbed[i - 1] != 1), flower_index[i] > i + 1, flower_index)
            if (i == 0 or flowerbed[i - 1] != 1) and flower_index[i] > i + 1:
                flowerbed[i] = 1
                planted += 1
                
            if planted >= n:
                break
        
        return planted >= n
            