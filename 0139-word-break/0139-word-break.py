class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @lru_cache(None)
        def findword(start):
            if(start == len(s)):
                return True
            
            for i in range(start, len(s)):
                if(s[start:i + 1] in word_set and findword(i + 1)):
                    return True
            
            return False
            
        word_set = set(wordDict)
        return findword(0)