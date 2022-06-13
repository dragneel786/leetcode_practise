class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = " ".join(sentence) + " "
        sMap = [0] * (len(s))
        for i in range(1, len(s)):
            sMap[i] = 1 if(s[i] == " ") else sMap[i - 1] - 1

        count = 0
        for r in range(rows):
            count += cols
            count += sMap[count % len(s)]

        return count // len(s)
            
                