class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        
        def word_hash(words):
            word_dict = defaultdict(list)
            for i, word in enumerate(words):
                word_dict[word[0]].append(i)
            return word_dict
        
        
        hash_word = word_hash(words)
        curr = deque()
        res = []
        for i, c in enumerate(text + '-'):
            n = len(curr)
            for _ in range(n):
                ci, wi, idx = curr.popleft()
            
                if(idx == len(words[wi])):
                    res.append([ci, ci + idx - 1])
                elif(words[wi][idx] == c):
                    curr.append((ci, wi, idx + 1))
            
            for wi in hash_word[c]:
                curr.append((i, wi, 1))
        
        return sorted(res)
                    