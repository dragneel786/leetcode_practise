class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ['a']
        while(len(word) < k):
            for i in range(len(word)):
                char_num = (ord(word[i]) - 96) % 25
                word.append(chr(97 + char_num))
         
        return word[k - 1]