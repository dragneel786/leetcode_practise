class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if(money < children):
            return -1
        
        money -= children
        if(money < 7):
            return 0
        # 13
        # 3
        if(money <= 7 * children):
            val = (money // 7)
            return val - (money % 7 == 3 and val == children - 1)
        
        return children - 1