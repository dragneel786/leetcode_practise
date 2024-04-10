class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = deque(sorted(deck))
        q = deque()
        while(deck):
            dummy = deque()
            dummy.append(deck.pop())
            if(q):
                dummy.append(q.pop())
                while(q):
                    dummy.append(q.popleft())
            
            q = dummy
        
        return q
            
        