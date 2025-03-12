package main

func numJewelsInStones(jewels string, stones string) int {
	jewelsMap := make(map[rune]struct{})

	for _, value := range jewels {
		jewelsMap[value] = struct{}{}
	}

	count := 0
	for _, key := range stones {
		_, ok := jewelsMap[key]
		if ok {
			count += 1
		}
	}
	return count
}

func main() {
	println(numJewelsInStones("aA", "aAAbbbb"))
}