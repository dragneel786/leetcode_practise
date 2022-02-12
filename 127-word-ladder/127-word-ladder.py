class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        seen = set()
        wordList = set(wordList)
        q.appendleft(beginWord)
        seen.add(beginWord)
        changes = 1
        
        def getChange(s, seen, q, wordList):
            alpha = "abcdefghijklmnopqrstuvwxyz"
            for i in range(len(s)):
                temp = list(s)
                for a in alpha:
                    temp[i] = a
                    val = ''.join(temp)
                    if(val in wordList and val not in seen):
                        seen.add(val)
                        q.appendleft(val)
        
        while(len(q)):
            for i in range(len(q)):
                word = q.pop()
                getChange(word, seen, q, wordList)
                if(endWord in seen):
                    return changes + 1
            changes += 1

        return 0