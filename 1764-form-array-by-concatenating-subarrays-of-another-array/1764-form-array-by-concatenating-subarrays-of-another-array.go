func canChoose(groups [][]int, nums []int) bool {
    rows := len(groups)
    que := list.New()
    for _, num := range nums {
        if groups[0][0] == num {
            que.PushBack([]int{0, 0})
        }
        
        for range que.Len() {
            element := que.Front()
            que.Remove(element)
            coor := element.Value.([]int)
            if coor[0] == rows {
                return true
            }
            
            if groups[coor[0]][coor[1]] == num { 
                coor[1]++ 
            } else { coor[1] = 0}
            
            if coor[1] == len(groups[coor[0]]){
                coor[0]++  
                coor[1] = 0
            }
            que.PushBack(coor)
        }
    }
    
    for range que.Len() {
        element := que.Front()
        que.Remove(element)
        coor := element.Value.([]int)
        if coor[0] == rows {
            return true
        }
    }
    
    return false
}