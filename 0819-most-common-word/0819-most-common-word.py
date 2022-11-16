class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        def create_counter(para):
            word = ""
            counter = Counter()
            for c in para:
                if(c.isalpha()):
                    word += c.lower()
                else:
                    if(len(word)):
                        counter[word] += 1
                    word = ""
            
            return counter
                
        
        para_counter = create_counter(paragraph + '-')
        print(para_counter)
        banned = set(banned)
        gc = 0
        gw = ""
        for w, c in para_counter.items():
            if(w not in banned and c > gc):
                gw = w
                gc = c
        
        return gw
        
        