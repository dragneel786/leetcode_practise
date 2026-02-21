package main

import (
    "math"
)

func countPrimeSetBits(left int, right int) int {
    count := 0

    for n := left; n <= right; n++ {
        bits := countBits(n)
        if isPrime(bits) {
            count++
        }
    }

    return count
}

func countBits(n int) int {
    bits := 0
    for n > 0 {
        bits += n & 1
        n >>= 1
    }
    return bits
}

func isPrime(n int) bool {
    if n < 2 {
        return false
    }

    limit := int(math.Sqrt(float64(n)))
    for i := 2; i <= limit; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}