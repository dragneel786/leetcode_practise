func losingPlayer(x int, y int) string {
    var turn = 1
    for x > 0 && y > 3 {
        x -= 1
        y -= 4
        turn *= -1
    }
    
    if turn == -1 {
        return "Alice"
    }
    
    return "Bob"
}