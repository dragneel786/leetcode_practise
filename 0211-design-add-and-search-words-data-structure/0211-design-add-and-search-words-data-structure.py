class WordDictionary:

    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str) -> None:
        temp_trie = self.trie
        for c in word:
            temp_trie[c] = temp_trie.get(c, {})
            temp_trie = temp_trie[c]
        temp_trie['$'] = None

    def search(self, word: str) -> bool:
        
        def search_it(w, t):
            if(t):
                for i, c in enumerate(w):
                    if(c == '.'):
                        for k in t.keys():
                            if(search_it(w[i + 1:], t[k])):
                                return True
                        return False
                    elif(c not in t):
                        return False
                    else:
                        t = t[c]
            
            return t != None and '$' in t
                
        return search_it(word, self.trie)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)