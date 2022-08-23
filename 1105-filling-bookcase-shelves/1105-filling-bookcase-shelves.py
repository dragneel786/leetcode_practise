class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        def arrange_books(idx, height, width):
            if(idx == len(books)):
                return height
            
            key = (idx, height, width)
            if(key in memo): return memo[key]
            
            wi, hi = books[idx]
            if(wi <= width):
                memo[key] = arrange_books(idx + 1,
                          max(height, hi), width - wi)
            
            memo[key] = min(memo[key], arrange_books(idx + 1,\
                                 hi, shelfWidth - wi) + height)
            
            return memo[key]
        
        memo = defaultdict(lambda:inf)
        return arrange_books(0, 0, shelfWidth)
            
            
        