class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        def insert_in_trie(temp, word):
            for c in word:
                if(c not in temp):
                    temp[c] = {}
                
                temp = temp[c] 
            temp['$'] = None
        
        
        def validate(t, w):
            if(not w):
                return True
            
            ans = False
            for i, c in enumerate(w):
                if(ans or c not in t):
                    break
                
                t = t[c]
                if('$' in t and validate(trie, w[i + 1:])):
                    ans = True
                    
            return ans
            
            
        
        words.sort(key=lambda x: len(x))
        trie = dict()
        ans = []
        for word in words:
            if(validate(trie, word)):
                ans.append(word)
                
            insert_in_trie(trie, word)
        
        return ans
                