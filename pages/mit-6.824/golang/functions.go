package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func mult(x, y int) int {
	return x*y
}

func main() {
	fmt.Println(add(42, 12))
	fmt.Println(mult(42, 12))
}
