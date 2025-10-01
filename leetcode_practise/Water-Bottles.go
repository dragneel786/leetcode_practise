func numWaterBottles(numBottles int, numExchange int) int {
    var totalBottles = 0
    var empty = 0
    for numBottles + empty >= numExchange {
        totalBottles += numBottles
        var temp = (numBottles + empty) / numExchange
        empty = (numBottles + empty) % numExchange
        // fmt.Println(totalBottles, empty, numBottles, temp)
        numBottles = temp
    }
    return totalBottles + numBottles
}