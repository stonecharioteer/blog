package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func mult(x, y int) int {
	return x * y
}

func swap(x, y string) (string, string) {
	return y, x
}

func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return // this returns the named variables x, y in that order.
}

func main() {
	fmt.Println(add(42, 12))
	fmt.Println(mult(42, 12))
	a, b := swap("hello", "world")
	fmt.Println(a, b)
	fmt.Println(split(17))
}
