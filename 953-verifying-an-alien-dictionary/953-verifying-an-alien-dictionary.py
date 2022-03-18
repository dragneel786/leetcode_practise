class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        maxL = 0
        for w in words:
            maxL = max(len(w), maxL)
        
        order_idx = [[order.index(ch) for ch in w] for w in words]
        return order_idx == sorted(order_idx, key=lambda o: o[0:maxL])