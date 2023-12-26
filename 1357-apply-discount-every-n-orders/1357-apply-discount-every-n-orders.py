class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.nth, self.curr = n, 0
        self.discount = discount
        self.product_price = dict()
        for pro, pri in zip(products, prices):
            self.product_price[pro] = pri
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        for p, a in zip(product, amount):
            total += a * self.product_price[p]
        
        self.curr += 1
        if(self.curr == self.nth):
            total = total * ((100 - self.discount) / 100)
            self.curr = 0
        
        return total
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)