class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = deque(sorted(deck))
        q = deque()
        while(deck):
            if(q):
                q.appendleft(q.pop())
            q.appendleft(deck.pop())
            
        return q
            
        