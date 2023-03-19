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
            if(w):
                if(w[0] != '.'):
                    if(w[0] not in t):
                        return False

                    return search_it(w[1:], t[w[0]])

                else:
                    for k in t.keys():
                        if(k != '$' and search_it(w[1:], t[k])):
                            return True
                    return False

            return '$' in t
                
        return search_it(word, self.trie)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)