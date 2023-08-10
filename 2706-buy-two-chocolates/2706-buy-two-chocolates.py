class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = second = inf        
        for m in prices:
            if(first > m):
                second = first
                first = m
            
            elif(second > m):
                second = m
        
        val = first + second
        return (money - val) if(val <= money) else money