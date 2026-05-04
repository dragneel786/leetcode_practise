func rotate(matrix [][]int)  {
    n := len(matrix)
    k := n - 1
    for i := range n - 1 {
        for j:=i; j < k - i; j++ {
            matrix[i][j], matrix[j][k-i], matrix[k-i][k-j], matrix[k-j][i] = matrix[k-j][i], matrix[i][j], matrix[j][k-i], matrix[k-i][k-j]
        }
    }
}