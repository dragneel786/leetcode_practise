class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = []
        for i, word in enumerate(sentence.split()):
            word_list = deque(list(word))
            if(word_list[0].lower() not in vowels):
                word_list.append(word_list.popleft())
            
            res.append(''.join(word_list) + 'ma' + 'a' * (i + 1))
        
        return ' '.join(res)
            
            
        