package main

func longestContinuousSubstring(s string) int {
	length := 1
	maxLength := -1
	for i := 0; i < len(s)-1; i++ {

		if rune(s[i])+1 == rune(s[i+1]) {
			length++
		} else {
			if length > maxLength {
				maxLength = length
			}
			length = 1
		}

	}
	if length > maxLength {
		maxLength = length
	}
	return maxLength
}

func main() {
	println(longestContinuousSubstring("abcde"))
}
