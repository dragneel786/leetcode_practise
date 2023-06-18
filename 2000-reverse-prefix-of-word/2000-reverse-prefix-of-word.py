class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = []
        for i, c in enumerate(word):
            ans.append(c)
            if(c == ch):
                break
        else:
            return word
        
        return ''.join(ans[::-1]) + word[i+1:]