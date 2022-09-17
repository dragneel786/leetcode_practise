class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        rmap = {w[::-1]:i for i, w in enumerate(words)}
        res = []

        for j, word in enumerate(words):
            for i in range(len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]

                if(suffix == suffix[::-1] and prefix in rmap):
                    if(j != rmap[prefix]):
                        res.append([j, rmap[prefix]])

                if(prefix and prefix == prefix[::-1] and suffix in rmap):
                    if(j != rmap[suffix]):
                        res.append([rmap[suffix], j])

        return res
            
                
                
                
                
                
                
    