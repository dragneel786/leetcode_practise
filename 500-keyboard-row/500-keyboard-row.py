class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        char_row_map = { c:i for i, row in enumerate(rows) for c in row}
        
        res = []
        for word in words:
            belongs = char_row_map[word[0].lower()]
            for w in word[1:]:
                w = w.lower()
                if(char_row_map[w] != belongs):
                    break
            else:
                res.append(word)
        
        return res
                    
        