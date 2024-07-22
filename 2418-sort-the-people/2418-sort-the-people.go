type Pair struct {
    Str string
    Num int
}

func sortPeople(names []string, heights []int) []string {
    var pairs = []Pair{}
    for i := range len(names) {
        pairs = append(pairs, Pair{names[i], heights[i]})
    }

    sort.Slice(pairs, func(i, j int) bool {
       return pairs[j].Num < pairs[i].Num
    })

    for i := range len(names){
        names[i] = pairs[i].Str
    }

    return names
}