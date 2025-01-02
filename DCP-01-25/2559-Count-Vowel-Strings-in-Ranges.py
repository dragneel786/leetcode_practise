class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = [1 if (words[0][0] in vowels and words[0][-1] in vowels) else 0]
        for i in range(1, len(words)):
            res.append(res[-1] + (words[i][0] in vowels and words[i][-1] in vowels))
        
        print(res)
        ret = []
        for a, b in queries:
            s = res[b]
            if a > 0:
                s -= res[a - 1]
            
            ret.append(s)
        
        return ret
            
            
