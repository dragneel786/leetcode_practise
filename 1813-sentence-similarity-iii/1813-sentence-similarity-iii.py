class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) < len(sentence2):
            return self.areSentencesSimilar(sentence2, sentence1)
        
        splits1 = sentence1.split()
        splits2 = sentence2.split()
        n1, n2 = len(splits1), len(splits2)
        
        idx1, idx2 = len(splits1) - 1, len(splits2) - 1
        while(idx1 > -1 and idx2 > -1 and\
              splits1[idx1] == splits2[idx2]):
            idx1 -= 1
            idx2 -= 1
        
        if idx2 < 0:
            return True
        
        bidx1 = bidx2 = 0
        while(bidx1 <= idx1 and bidx2 <= idx2\
              and splits1[bidx1] == splits2[bidx2]):
            bidx1 += 1
            bidx2 += 1
        
        # print(idx1, idx2, bidx1, bidx2, no_match)
        return bidx2 > idx2
        
        
        
        
            