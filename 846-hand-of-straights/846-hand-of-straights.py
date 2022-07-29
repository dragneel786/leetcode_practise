class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if(n % groupSize > 0):
            return False
        
        hand.sort()
        C = Counter(hand)
        for h in hand:
            count = 0
            while(C[h] and count < groupSize):
                C[h] -= 1
                count += 1
                h += 1
                
            if(count != 0 and count != groupSize):
                return False
            
        return True
                
            