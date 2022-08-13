class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        words_hash = Counter(words)
        window = len(words[0])
        words_len = len(words)
        res = []
        for i in range(len(s)):
            temp = Counter()
            temp_len = words_len
            start = i
            while(s[start: start + window] in  words_hash\
                 and temp_len):
                temp[s[start: start + window]] += 1
                start += window
                temp_len -= 1
            
            if(words_hash == temp):
                res.append(i)
        
        return res
                
        
        