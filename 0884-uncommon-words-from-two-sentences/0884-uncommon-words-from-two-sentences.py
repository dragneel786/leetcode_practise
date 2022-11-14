class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uniq, dup = set(), set()
        for a in [*s1.split(), *s2.split()]:
            if(a not in uniq):
                uniq.add(a)
            else:
                dup.add(a)
        
        return uniq - dup