func longestSubarray(nums []int, limit int) int {
    var maxQue = list.New()
    var minQue = list.New()
    var i = 0
    for _, num := range nums {
        for maxQue.Len() > 0 && maxQue.Back().Value.(int) < num {
            maxQue.Remove(maxQue.Back())
        }

        for minQue.Len() > 0 && minQue.Back().Value.(int) > num {
            minQue.Remove(minQue.Back())
        }
        
        maxQue.PushBack(num)
        minQue.PushBack(num)

        if (maxQue.Front().Value.(int) - minQue.Front().Value.(int)) > limit {
            if maxQue.Front().Value.(int) == nums[i] { maxQue.Remove(maxQue.Front()) }
            if minQue.Front().Value.(int) == nums[i] { minQue.Remove(minQue.Front()) }
            i += 1
        }
    }

    return len(nums) - i
}