class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        corder = {c:i for i, c in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            for a, b in zip(w1, w2):
                # print(a, b, corder[a], corder[b])
                if(corder[a] < corder[b]):
                    break
                    
                if(corder[a] > corder[b]):
                    return False
            else:
                if(len(w1) > len(w2)):
                    return False
        return True