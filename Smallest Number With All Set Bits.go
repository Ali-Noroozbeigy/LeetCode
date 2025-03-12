package main

import (
	"math"
	"strconv"
)

func smallestNumber(n int) int {
	binary := strconv.FormatInt(int64(n), 2)
	return int(math.Pow(2, float64(len(binary)))) - 1
}

func main() {
	println(smallestNumber(10))
}
