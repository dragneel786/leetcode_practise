type Bank struct {
    accountBalances *[]int64
}


func Constructor(balance []int64) Bank {
    return Bank{
        accountBalances: &balance,
    }
}


func (this *Bank) Transfer(account1 int, account2 int, money int64) bool {
    var accountInfo = this.accountBalances
    var size = len(*accountInfo)
    if account1 > size || account2 > size {
        return false
    }
    
    if (*accountInfo)[account1 - 1] < money {
        return false
    }
    
    (*accountInfo)[account1 - 1] -= money
    (*accountInfo)[account2 - 1] += money
    return true
}


func (this *Bank) Deposit(account int, money int64) bool {
    var accountInfo = this.accountBalances
    var size = len(*accountInfo)
    if account > size {
        return false
    }
    
    (*accountInfo)[account - 1] += money
    return true
}


func (this *Bank) Withdraw(account int, money int64) bool {
    var accountInfo = this.accountBalances
    var size = len(*accountInfo)
    if account > size {
        return false
    }
    
    if (*accountInfo)[account - 1] < money {
        return false
    }
    
    (*accountInfo)[account - 1] -= money
    return true
}


/**
 * Your Bank object will be instantiated and called as such:
 * obj := Constructor(balance);
 * param_1 := obj.Transfer(account1,account2,money);
 * param_2 := obj.Deposit(account,money);
 * param_3 := obj.Withdraw(account,money);
 */