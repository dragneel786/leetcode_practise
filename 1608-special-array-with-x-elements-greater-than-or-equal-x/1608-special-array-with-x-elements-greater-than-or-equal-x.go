func specialArray(nums []int) int {
    slices.Sort(nums)
    var binSearch = func (val int) int {
        var low, high = 0, len(nums) - 1
        for low <= high {
            var mid = low + ((high - low) / 2)
            if nums[mid] >= val {
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        return low
    }
    
    var left, right = 0, 1001
    for left <= right {
        var midVal = left + ((right - left) / 2)
        var binIndex = binSearch(midVal)
        if midVal == len(nums) - binIndex {
            return midVal
        }
        
        if midVal < len(nums) - binIndex {
            left = midVal + 1
        } else {
            right = midVal - 1
        }
    }
    
    return -1
}