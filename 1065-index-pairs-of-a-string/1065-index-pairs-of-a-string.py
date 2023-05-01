class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        
        def create_trie():
            t = dict()
            for word in words:
                temp = t
                for c in word:
                    temp[c] = temp.get(c, {})
                    temp = temp[c]
                
                temp['$'] = None
            
            return t
        
        trie = create_trie()
        ans = []
        for i in range(len(text)):
            temp = trie
            for j in range(i, len(text)):
                if(text[j] not in temp):
                    break
                
                temp = temp[text[j]]
                if('$' in temp):
                    ans.append([i, j])
                
    
        return ans
                
                    
        
                    