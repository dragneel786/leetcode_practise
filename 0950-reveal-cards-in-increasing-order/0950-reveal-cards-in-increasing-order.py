class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        q = deque([i for i in range(n)])
        res = [0] * n
        deck.sort()
        i = 0
        flip = True
        while(q):
            if(flip):
                idx = q.popleft()
                res[idx] = deck[i]
                i += 1
            else:
                q.append(q.popleft())
            
            flip = not flip
        
        return res