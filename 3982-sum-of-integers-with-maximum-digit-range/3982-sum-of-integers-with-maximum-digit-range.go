func maxDigitRange(nums []int) int {
    maxRange, maxDiff := 0, 0
    for _, num := range nums {
        maxVal, minVal := 0, 9
        temp := num
        for temp > 0 {
            rem := temp % 10
            if maxVal < rem {
                maxVal = rem
            }

            if minVal > rem {
                minVal = rem
            }

            temp /= 10
        }
        diff := maxVal - minVal
        if diff > maxDiff {
            maxRange = num
            maxDiff = diff
        } else if diff == maxDiff {
            maxRange += num
        }
    }
    return maxRange   
}