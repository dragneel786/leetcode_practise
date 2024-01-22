class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        def form_sub(idx, values = ''):
            if(idx >= len(words)):
                return get_score(values)
            
            return max(form_sub(idx + 1, values + words[idx]),\
                       form_sub(idx + 1, values))
        
        
        def get_score(word):
            letter_copy = Counter(letters)
            values = 0
            for c in word:
                if(not letter_copy[c]):
                    return 0

                letter_copy[c] -= 1
                values += score[ord(c) - 97]
                
            return values
        
        
        return form_sub(0)
                
                    
            