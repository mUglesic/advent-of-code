package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	"time"
)

type equation struct {
	result int
	nums []int
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readLinesFromFile(fileName string) ([][]byte) {

	f, err := os.Open(fileName)
	check(err)
	defer f.Close()

	var lines [][]byte

	sc := bufio.NewScanner(f)

	for sc.Scan() {
		lines = append(lines, []byte(sc.Text()))
	}

	return lines

}

func checkSolvable(eq equation, i int, currentResult int) (bool) {

	if eq.result == currentResult && i == len(eq.nums) {
		return true
	}

	if i >= len(eq.nums) || currentResult > eq.result {
		return false
	}

	return checkSolvable(eq, i + 1, currentResult + eq.nums[i]) || checkSolvable(eq, i + 1, currentResult * eq.nums[i])

}

func solve(data [][]byte) (int) {

	var eqs []equation

	for _, s := range data {
		split := strings.Split(string(s), ": ")

		testVal, err := strconv.Atoi(split[0])
		check(err)

		ns := strings.Split(split[1], " ")
		var nums []int
		for _, n := range ns {
			num, err := strconv.Atoi(string(n))
			check(err)
			nums = append(nums, num)
		}

		eqs = append(eqs, equation{testVal, nums})

	}

	sum := 0

	for _, eq := range eqs {

		if checkSolvable(eq, 1, eq.nums[0]) {
			sum += eq.result
		}

	}

	return sum

}

func intConcat(a int, b int) (int) {

	return int(a * int(math.Pow10(1 + int(math.Floor((math.Log10(float64(b))))))) + b)

}

func checkSolvableConcat(eq equation, i int, currentResult int) (bool) {

	if eq.result == currentResult && i == len(eq.nums) {
		return true
	}

	if i >= len(eq.nums) || currentResult > eq.result {
		return false
	}

	return checkSolvableConcat(eq, i + 1, currentResult + eq.nums[i]) || checkSolvableConcat(eq, i + 1, currentResult * eq.nums[i]) || checkSolvableConcat(eq, i + 1, intConcat(currentResult, eq.nums[i]))

}

func solve2(data [][]byte) (int) {

	var eqs []equation

	for _, s := range data {
		split := strings.Split(string(s), ": ")

		testVal, err := strconv.Atoi(split[0])
		check(err)

		ns := strings.Split(split[1], " ")
		var nums []int
		for _, n := range ns {
			num, err := strconv.Atoi(string(n))
			check(err)
			nums = append(nums, num)
		}

		eqs = append(eqs, equation{testVal, nums})

	}

	sum := 0

	for _, eq := range eqs {

		if checkSolvableConcat(eq, 1, eq.nums[0]) {
			sum += eq.result
		}

	}

	return sum

}

func main() {

	start := time.Now()

	data := readLinesFromFile(os.Args[1])

	// result := solve(data)
	result := solve2(data)

	fmt.Println(result)

	elapsed := time.Since(start)

	fmt.Printf("Runtime: %s\n", elapsed)

}