func numSteps(s string) int {
    var que = list.New()
    for _, c := range s {
        que.PushFront(string(c))
    }
    
    var steps = 0
    for que.Len() > 1 {
        var temp = que.Front()
        if temp.Value.(string) == "1" {

            for temp != nil && temp.Value.(string) == "1" {
                temp.Value = "0"
                temp = temp.Next()
            }
    
            if temp != nil {
                temp.Value = "1"
            } else {
                que.PushBack("1")
            }
            steps++
        }
        var element = que.Front()
        que.Remove(element)
        steps++
    }

    return steps
}