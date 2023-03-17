class Trie:

    def __init__(self):
        self.core = dict()
        

    def insert(self, word: str) -> None:
        tcore = self.core
        for c in word:
            tcore[c] = tcore.get(c, {})
            tcore = tcore[c]
        tcore["$"] = None

    def search(self, word: str) -> bool:
        tcore = self.core
        for c in word:
            if(c not in tcore):
                return False
            tcore = tcore.get(c, {})
        return '$' in tcore
        

    def startsWith(self, prefix: str) -> bool:
        tcore = self.core
        for c in prefix:
            if(c not in tcore):
                return False
            tcore = tcore.get(c, {})
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)