class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        @cache
        def min_height(i):
            if i >= len(books):
                return 0
            
            max_h = tot_thick = 0
            ret = inf
            for j in range(i, len(books)):
                tot_thick += books[j][0]
                if tot_thick > shelfWidth:
                    break

                max_h = max(max_h, books[j][1])
                ret = min(ret, max_h + min_height(j + 1))

            return ret
            
        
        return min_height(0)
            
        
        