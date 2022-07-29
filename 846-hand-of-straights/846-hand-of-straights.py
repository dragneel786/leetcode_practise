class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if(n % groupSize > 0):
            return False
        
        C = Counter(hand)
        for h in sorted(hand):
            if(C[h] > 0):
                for j in range(groupSize - 1, -1, -1):
                    C[h + j] -= C[h]
                    if(C[h + j] < 0):
                        return False
        return True
                
            