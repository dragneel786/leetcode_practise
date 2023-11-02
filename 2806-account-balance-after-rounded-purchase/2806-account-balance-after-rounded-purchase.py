from decimal import Decimal, ROUND_HALF_UP
class Solution:
    def accountBalanceAfterPurchase(self, x: int) -> int:
        x = Decimal(x / 10)
        return 100 - (x.quantize(Decimal('1'), rounding=ROUND_HALF_UP) * 10)
        