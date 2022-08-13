class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        def check_present(start):
            remaining = words_hash.copy()
            substr = s[start: start + window]
            words_used = 0
            
            while(remaining[substr] > 0):
                remaining[substr] -= 1
                start += window
                substr = s[start: start + window]
                words_used += 1
            
            return words_used == words_len
        
        
        words_hash = Counter(words)
        window = len(words[0])
        words_len = len(words)
        substring_size = window * words_len
        res = []
        
        for i in range(len(s) - substring_size + 1):
            if(check_present(i)):
                res.append(i)
            
        return res
                
        
        