class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if (words[startIndex] == target):
            return 0

        n = len(words)
        words.extend(words)
        steps = 1
        i = n + startIndex - 1
        j = startIndex + 1
        while (i > -1 and j < 2 * n):
            if (words[i] == target or words[j] == target):
                return steps

            if (i > -1):
                i -= 1

            if (j < 2 * n):
                j += 1

            steps += 1

        return -1

        
            