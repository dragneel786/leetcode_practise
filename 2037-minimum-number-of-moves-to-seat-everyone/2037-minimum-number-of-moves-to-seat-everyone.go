func minMovesToSeat(seats []int, students []int) int {
    slices.Sort(seats)
    slices.Sort(students)
    var moves = 0
    for i := range len(seats) {
        moves += int(math.Abs(float64(seats[i] - students[i])))
    }
    
    return moves
}
