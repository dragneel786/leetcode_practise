class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def append_new_word(word, weight):
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i + 1:]
                    if(not word_count[new_word]):
                        continue
                        
                    word_count[new_word] -= 1
                    q.append((new_word, weight + 1))
                    
                    
        word_count = Counter(wordList)
        q = deque([(beginWord, 1)])
        while(q):
            for _ in range(len(q)):
                pop_word, pop_len = q.popleft()
                if(pop_word == endWord):
                    return pop_len
                
                append_new_word(pop_word, pop_len)
                
        return 0

        
        