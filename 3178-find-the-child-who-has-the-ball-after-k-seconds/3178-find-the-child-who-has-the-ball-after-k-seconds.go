func numberOfChild(n int, k int) int {
    var div = k / (n - 1)
    var mod = k % (n - 1)
    fmt.Println(div, mod)
    if mod == 0 {
        if div % 2 == 1 {
            return n - 1
        }
        return 0
    }
    
    if div % 2 == 1 {
        return (n - mod - 1)
    }
    
    return mod
}