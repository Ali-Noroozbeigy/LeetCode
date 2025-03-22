package main

import "fmt"

func queryResults(limit int, queries [][]int) []int {
	var result []int
	ballsColor := make(map[int]int)
	colorCount := make(map[int]int)
	for _, query := range queries {
		if prevColor, ok := ballsColor[query[0]]; ok {
			colorCount[prevColor]--
			if colorCount[prevColor] == 0 {
				delete(colorCount, prevColor)
			}
		}
		colorCount[query[1]]++
		ballsColor[query[0]] = query[1]
		result = append(result, len(colorCount))
	}

	return result
}

func main() {
	fmt.Println(queryResults(4, [][]int{{1, 4}, {2, 5}, {1, 3}, {3, 4}}))
}
