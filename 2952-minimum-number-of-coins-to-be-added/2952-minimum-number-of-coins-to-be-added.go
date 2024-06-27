func minimumAddedCoins(coins []int, target int) int {
    var obtain, res = 0, 0
    slices.Sort(coins)
    for i := 0; i < len(coins) && obtain <= target; i++ {
        for obtain + 1 < coins[i] {
            obtain += obtain + 1
            res++
        }
        obtain += coins[i]
    }
    
    for obtain < target {
        obtain += obtain + 1
        res++
    }
    
    return res
}