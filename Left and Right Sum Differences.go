package main

import (
	"fmt"
	"math"
)

func leftRightDifference(nums []int) []int {
	var leftSum []int
	var rightSum []int

	leftSum = append(leftSum, 0)
	sum := 0
	for i := 1; i < len(nums); i++ {
		sum += nums[i-1]
		leftSum = append(leftSum, sum)
	}

	sum = 0
	rightSum = append(rightSum, 0)
	for i := len(nums) - 1; i > 0; i-- {
		sum += nums[i]
		rightSum = append(rightSum, 0)
		copy(rightSum[1:], rightSum)
		rightSum[0] = sum
	}

	var answer []int
	for i := 0; i < len(nums); i++ {
		answer = append(answer, int(math.Abs(float64(leftSum[i]-rightSum[i]))))
	}
	return answer
}

func main() {
	fmt.Println(leftRightDifference([]int{1}))
}
