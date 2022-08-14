class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def construct_seq(curr_word, op = []):
            nonlocal res
            if(curr_word == beginWord):
                op.append(beginWord)
                res.append(op[::-1])
                return
            
            for word in graph[curr_word]:
                construct_seq(word, op + [curr_word])
            
            
        def valid_words(word):
            ret = []
            for i in range(len(word)):
                for c in ascii_lowercase:
                    new_word = word[:i] + c + word[i + 1:]
                    if(new_word in wordList):
                        ret.append(new_word)
                        
            return ret
                    
            
        def get_smallest_seq():
            nonlocal wordList
            curr_level = {beginWord}
            
            while(curr_level):
                wordList -= curr_level
                next_level = set()
                for node in curr_level:
                    if(node == endWord):
                        return
                    
                    for word in valid_words(node):
                        next_level.add(word)
                        graph[word].append(node)
                
                curr_level = next_level
        
        
        res = []
        wordList = set(wordList)
        graph = defaultdict(list)
        
        if(endWord in wordList):
            wordList.discard(beginWord)
            get_smallest_seq()
            construct_seq(endWord)
        
        return res
        
        
        
        
        
        
        
        