package main

import (
	"fmt"
	"slices"
	"sort"
)

func minProcessingTime(processorTime []int, tasks []int) int {
	sort.Sort(sort.Reverse(sort.IntSlice(tasks)))
	sort.Ints(processorTime)

	var result []int
	processorID := 0

	for i := 0; i < len(tasks); i += 4 {
		result = append(result, processorTime[processorID]+max(tasks[i], tasks[i+1], tasks[i+2], tasks[i+3]))
		processorID++
	}

	return slices.Max(result)
}

func main() {
	fmt.Println(minProcessingTime([]int{10, 20}, []int{2, 3, 1, 2, 5, 8, 4, 3}))
}
