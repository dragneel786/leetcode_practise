type Queue struct {
    items []string
}

func (que *Queue) Enque(val string) {
    que.items = append(que.items, val)
}

func (que *Queue) Deque() string {
    if len(que.items) == 0 {
        return ""
    }
    
    val := que.items[0]
    que.items = que.items[1:]
    return val
}

func NewQueue() *Queue {
    return &Queue{items: make([]string, 0)}
}

func openLock(deadends []string, target string) int {
    hashSet := make(map[string]bool)
    for _, dead := range deadends {
        hashSet[dead] = true
    }
    
    steps := 0
    queue := NewQueue()
    queue.Enque("0000")
    for len(queue.items) > 0 {
        for range queue.items {
            combo := queue.Deque()
            if hashSet[combo] {
                continue
            }
            hashSet[combo] = true
            if combo == target {
                return steps
            }
            spinLock(combo, queue, hashSet)
        }
        steps += 1
    }
    
    return -1
}

func spinLock(combo string, queue *Queue, hashSet map[string]bool){
    for i, char := range combo {
        num := int(char - '0')
        spinBack := (num - 1)
        spinFront := (num + 1) % 10
        if spinBack < 0 {
            spinBack = 9
        }
        str1 := combo[:i] + strconv.Itoa(int(spinBack)) + combo[i + 1:]
        if hashSet[str1] == false {
            queue.Enque(str1)
        }
        
        str2 := combo[:i] + strconv.Itoa(int(spinFront)) + combo[i + 1:]
        if hashSet[str2] == false{
            queue.Enque(str2)
        }
    }
}