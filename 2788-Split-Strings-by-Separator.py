class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            for w in word.split(separator):
                if w: res.append(w)
        
        return res
        