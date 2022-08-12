class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        
        def create_trie(words):
            trie = dict()
            for word in words:
                temp = trie
                for w in word:
                    temp[w] = temp.get(w, dict())
                    temp = temp[w]
                temp['$'] = None
            return trie

        def move_pointers(pointers, ch):
            for p in range(len(pointers)):
                trie, start, end = pointers.popleft()
                if('$' in trie):
                    marker[start] += 1
                    marker[end + 1] -= 1
                    start = end + 1

                if(ch in trie):
                    pointers.append([trie[c], start, end + 1])
        
        def construct_string(marker):
            is_open = False
            res = temp = ""
            for i,m in enumerate(marker):
                if(m != 0):
                    if(not is_open):
                        is_open = True
                    temp += s[i]
                else:
                    if(is_open):
                        res += "<b>" + temp + "</b>"
                        temp = ""
                        is_open = False
                    res += s[i] if(s[i] != "%") else ""
            return res
                    
        
        words_trie = create_trie(words)
        n = len(s)
        marker = [0] * (n + 1)
        pointers = deque()
        s += "%"
        for i, c in enumerate(s):
            move_pointers(pointers, c)
            if(c in words_trie):
                pointers.append([words_trie[c], i, i])

        for i in range(1, n + 1):
            marker[i] += marker[i - 1]
        
        return construct_string(marker)
        
        
        
        
        
            
                    
                    
                        
            