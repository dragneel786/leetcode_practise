class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return ''.join(["*" if c in "aeiou" else c for c in word])
        
        def query(word):
            if word in word_perfect:
                return word
            
            word_lower = word.lower()
            if word_lower in word_cap:
                return word_cap[word_lower]
            
            vowel = devowel(word_lower)
            if vowel in word_vow:
                return word_vow[vowel]
            
            return ""
            
        
        word_perfect = set(wordlist)
        word_cap = {}
        word_vow = {}
        
        for word in wordlist:
            word_lower = word.lower()
            word_cap.setdefault(word_lower, word)
            word_vow.setdefault(devowel(word_lower), word)
        
        return map(query, queries)
        
        