class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = dict()
        for i, b in enumerate(balance):
            self.accounts[i + 1] = b
        # print(self.accounts)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in self.accounts or account2 not in self.accounts:
            return False
        
        if self.accounts[account1] < money:
            return False
        
        self.accounts[account1] -= money
        self.accounts[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account not in self.accounts:
            return False
        
        self.accounts[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if self.accounts.get(account, 0) < money:
            return False
        
        self.accounts[account] -= money
        return True
        

        
        

        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)