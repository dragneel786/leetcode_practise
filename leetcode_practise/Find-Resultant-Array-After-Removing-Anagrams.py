class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            prev = "" if len(res) == 0 else res[-1]
            if sorted(list(word)) == sorted(list(prev)):
                continue
            
            res.append(word)
        
        return res