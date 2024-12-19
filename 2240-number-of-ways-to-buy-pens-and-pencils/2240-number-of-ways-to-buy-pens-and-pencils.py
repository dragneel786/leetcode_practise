class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost2 > cost1:
            return self.waysToBuyPensPencils(total, cost2, cost1)
        
        ways = 0
        count1 = 0
        while(total - (count1 * cost1) >= cost2):
            count2 = (total - (count1 * cost1)) // cost2
            # print(count2)
            ways += (count2 + 1)
            count1 += 1
        
        ways += (total >= (count1 * cost1))
        
        return ways