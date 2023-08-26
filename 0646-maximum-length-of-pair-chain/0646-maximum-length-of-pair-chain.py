class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        @lru_cache(None)
        def longest_chain(i = 0, prev = -1001):
            if(i == len(pairs)):
                return 0
            
            ret = -inf
            if(prev < pairs[i][0]):
                ret = 1 + longest_chain(i + 1, pairs[i][1])
            
            return max(ret, longest_chain(i + 1, prev))
        
        
        pairs.sort()
        return longest_chain()