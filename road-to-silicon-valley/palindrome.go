package main

import (
	"fmt"
)

func main() {
	firstCase := "babad"        // aba
	secondCase := "cbbd"        // bb
	thirdCase := "abacdfgdcaba" // aba

	palindromatic9000(firstCase)
	palindromatic9000(secondCase)
	palindromatic9000(thirdCase)
}

func palindromatic9000(normalString string) {
	invertedString := invertedString(normalString)
	var palindrome string
	var tmpPalindrome string
	count := 0
	for count < len(normalString) {
		if string(normalString[count]) == string(invertedString[count]) {
			if validateNewestPalindrome(tmpPalindrome, string(normalString[count])) {
				palindrome = tmpPalindrome + string(normalString[count])
			}
			tmpPalindrome = tmpPalindrome + string(normalString[count])
		}
		count++
	}
	fmt.Println(palindrome)
}
func validateNewestPalindrome(currentPalindrome, newStr string) bool {
	newPalindrome := currentPalindrome + newStr
	middle := len(currentPalindrome+newStr) / 2
	if len(currentPalindrome+newStr) == 2 {
		return newPalindrome[:middle] == invertedString(newPalindrome[middle:])
	}
	return newPalindrome[:middle+1] == invertedString(newPalindrome[middle:])
}
func invertedString(str string) string {
	count := 0
	var inverted string
	for count <= len(str)-1 {
		inverted = string(str[count]) + inverted
		count++
	}
	return inverted
}
