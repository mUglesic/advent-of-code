package main

import (
	"bufio"
	"fmt"
	"os"
	"time"
)

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

func solve(data [][]byte) (int) {

	return -1

}

func main() {

	start := time.Now()

	data := readLinesFromFile(os.Args[1])

	result := solve(data)
	// result := solve2(data)

	fmt.Println(result)

	elapsed := time.Since(start)

	fmt.Printf("Runtime: %s\n", elapsed)

}