class Solution:
    def countValidWords(self, sentence: str) -> int:
        
        count = 0
        for token in sentence.split(" "):
            n = len(token)
            if(not n):
                continue

            hypn = punc = 0
            for i, c in enumerate(token):
                hypn += c == '-'
                punc += c in '!,.'
                if(c.isdigit() or hypn > 1 or punc > 1):
                    break

                if(c in '!,.' and i != n - 1):
                    break

                if(c == '-' and \
                ((i == n - 1 or not token[i + 1].isalpha()) or \
                 (i == 0 or not token[i - 1].isalpha()))):
                    break
            
            else:
                 count += 1
            
        return count