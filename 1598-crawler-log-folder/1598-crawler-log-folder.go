func minOperations(logs []string) int {
    var que = list.New()
    for _, log := range logs {
        if log == "../" {
            if que.Len() > 0 {
                que.Remove(que.Back())
            }
        } else if log == "./" {
            continue
        } else {
            que.PushBack(log)
        }
    }

    return que.Len()
}