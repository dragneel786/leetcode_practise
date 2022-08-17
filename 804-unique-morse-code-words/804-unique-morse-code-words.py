class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        def transform(word):
            morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",\
                          ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",\
                          "...","-","..-","...-",".--","-..-","-.--","--.."]
            
            return "".join([morse_code[ord(c) - 97] for c in word])
        
        
        unique = set()
        for word in words:
            unique.add(transform(word))
        
        return len(unique)
        