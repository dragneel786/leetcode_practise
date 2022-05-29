class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxProd = 0
        n = len(words)

        def compare(w1, w2):
            for k in w1:
                if(k in w2):
                    return False
            return True

        for i in range(n - 1):
            for j in range(i + 1, n):
                if(compare(set(words[i]), set(words[j]))):
                    maxProd = max(len(words[i]) * len(words[j]), maxProd)

        return maxProd