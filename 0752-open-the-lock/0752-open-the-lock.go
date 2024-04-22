type Queue []string

func (q *Queue) Enqueue(val string) {
	*q = append(*q, val)
}

func (q *Queue) Dequeue() string {
	if len(*q) == 0 {
		return ""
	}
	val := (*q)[0]
	*q = (*q)[1:]
	return val
}

func NewQueue() *Queue {
	return &Queue{}
}

func openLock(deadends []string, target string) int {
	deadSet := make(map[string]bool)
	for _, dead := range deadends {
		deadSet[dead] = true
	}

	steps := 0
	queue := NewQueue()
	queue.Enqueue("0000")

	for len(*queue) > 0 {
		size := len(*queue)
		for i := 0; i < size; i++ {
			combo := queue.Dequeue()
			if deadSet[combo] {
				continue
			}
			if combo == target {
				return steps
			}
            deadSet[combo] = true
			spinLock(combo, queue, deadSet)
		}
		steps++
	}
	return -1
}

func spinLock(combo string, queue *Queue, deadSet map[string]bool) {
	for i, char := range combo {
		num := int(char - '0')
		spinBack := (num - 1 + 10) % 10
		spinFront := (num + 1) % 10

		str1 := combo[:i] + strconv.Itoa(spinBack) + combo[i+1:]
		if !deadSet[str1] {
			queue.Enqueue(str1)
		}

		str2 := combo[:i] + strconv.Itoa(spinFront) + combo[i+1:]
		if !deadSet[str2] {
			queue.Enqueue(str2)
		}
	}
}