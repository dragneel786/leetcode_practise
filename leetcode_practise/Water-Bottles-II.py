class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty_bottles, bottle_drunks = 0, 0
        while((numBottles + empty_bottles) >= numExchange):
            bottle_drunks += numBottles
            empty_bottles += numBottles
            numBottles = 0
            while(empty_bottles >= numExchange):
                empty_bottles -= numExchange
                numBottles += 1
                numExchange += 1
        
        return bottle_drunks + numBottles





