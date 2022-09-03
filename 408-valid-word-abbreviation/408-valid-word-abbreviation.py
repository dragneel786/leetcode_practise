class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        word_size = len(word)
        abbr_size = len(abbr)

        wi = ai = 0
        skip = ""
        while(wi < word_size and ai < abbr_size):

            while(ai < abbr_size and abbr[ai].isdigit()):
                if(not skip and int(abbr[ai]) == 0):
                    return False

                skip += abbr[ai] 
                ai += 1

            if(skip):
                if(wi + int(skip) > word_size):
                    return False
                wi += int(skip)
                skip = ""
                continue

            if(wi < word_size and word[wi] != abbr[ai]):
                return False

            ai += 1
            wi += 1

        return wi == word_size and ai == abbr_size
            
            
        
        
                
                
                
        
        