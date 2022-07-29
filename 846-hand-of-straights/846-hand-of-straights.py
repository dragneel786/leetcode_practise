class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        C = Counter(hand)
        prev, opened = -1, 0
        start = deque()
        for h in sorted(C):
            if(opened > C[h] or (opened > 0 and h > prev + 1)): return False
            start.append(C[h] - opened)
            prev, opened = h, C[h]
            if(len(start) == groupSize): opened -= start.popleft()
        return opened == 0