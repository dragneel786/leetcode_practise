class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        def transform(word):
            morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",\
                          ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",\
                          "...","-","..-","...-",".--","-..-","-.--","--.."]
            
            return "".join([morse_code[ord(c) - 97] for c in word])
        
        
        unique = {transform(word) for word in words}
        return len(unique)
        