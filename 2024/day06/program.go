package main

import (
	"bufio"
	"fmt"
	"os"
	"time"
)

type direction struct {
	x int
	y int
}

type location struct {
	field byte
	dirs []direction
}

var (
	UP = direction{x: 0, y: -1}
	RIGHT = direction{x: 1, y: 0}
	DOWN = direction{x: 0, y: 1}
	LEFT = direction{x: -1, y: 0}
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

func make2DArray[T any](h int, w int, def T) ([][]T) {

	a := make([][]T, h)
	for i := range a {
		a[i] = make([]T, w)
		for j := range a[i] {
			a[i][j] = def
		}
	}

	return a
	
}

func copy2DArray[T any](arr [][]T) ([][]T) {

	duplicate := make([][]T, len(arr))
	for i := range arr {
		duplicate[i] = make([]T, len(arr[i]))
		copy(duplicate[i], arr[i])
	}
	return duplicate

}

func print2DArray[T any](arr [][]T) {

	for _, line := range arr {
		for _, val := range line {
			fmt.Print(val)
		}
		fmt.Println()
	}

}

func arrayContains[T comparable](arr []T, e T) (bool) {

	for _, el := range arr {
		if el == e {
			return true
		}
	}

	return false

}

func findStart(data [][]byte) (int, int) {

	for i, line := range data {

		for j, element := range line {

			if element == '^' {
				return i, j
			}

		}

	}

	return -1, -1

}

func checkBounds(i int, j int, height int, width int) (bool) {

	return i >= 0 && i < height && j >= 0 && j < width

}

func turnRight(dir direction) (direction) {

	switch dir {
	case UP:
		return RIGHT
	case RIGHT:
		return DOWN
	case DOWN:
		return LEFT
	case LEFT:
		return UP
	default:
		return UP
	}

}

func solve(data [][]byte) (int, [][]rune) {

	height := len(data)
	width := len(data[0])

	visited := make2DArray(height, width, '.')

	i, j := findStart(data)
	dir := UP
	visited[i][j] = 'X'

	count := 1

	for checkBounds(i + dir.y, j + dir.x, height, width) {

		if data[i + dir.y][j + dir.x] == '#' {
			dir = turnRight(dir)
		} else {
			i, j =  i + dir.y, j + dir.x
			if visited[i][j] != 'X' {
				count++
				visited[i][j] = 'X'
			}
		}

	}

	// print2DArray(visited)

	return count, visited

}

func createOptions(data [][]byte) ([][][]byte) {

	_, visited := solve(data)
	iStart, jStart := findStart(data)

	var options [][][]byte

	for i, line := range data {
		for j, val := range line {

			if i == iStart && j == jStart {
				continue
			}

			if val == '.' && visited[i][j] == 'X' {
				dataCopy := copy2DArray(data)
				dataCopy[i][j] = '#'
				options = append(options, dataCopy)
			}

		}
	}

	return options

}

func solve2(data [][]byte) (int) {

	height := len(data)
	width := len(data[0])

	options := createOptions(data)

	iStart, jStart := findStart(data)

	count := 0

	for _, option := range options {

		visited := make2DArray(height, width, location{field: '.', dirs: make([]direction, 0)})

		i, j := iStart, jStart

		dir := UP
		visited[i][j].field = 'X'
		visited[i][j].dirs = append(visited[i][j].dirs, dir)

		// print2DArray(visited)

		for checkBounds(i + dir.y, j + dir.x, height, width) {

			if option[i + dir.y][j + dir.x] == '#' {
				dir = turnRight(dir)
			} else {

				i, j = i + dir.y, j + dir.x

				if visited[i][j].field == 'X' && arrayContains(visited[i][j].dirs, dir) {
					count++
					break
				}

				visited[i][j].field = 'X'
				visited[i][j].dirs = append(visited[i][j].dirs, dir)

			}

		}

	}

	return count

}

func main() {

	start := time.Now()

	data := readLinesFromFile(os.Args[1])

	// result, _ := solve(data)
	result := solve2(data)

	fmt.Println(result)

	elapsed := time.Since(start)

	fmt.Printf("Runtime: %s\n", elapsed)

}
