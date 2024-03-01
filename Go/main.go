package main

import "github.com/daniial79/LeetCode-Problems/stack"

func main() {
	myStack := stack.Constructor()

	myStack.Push(0)
	myStack.Push(1)
	myStack.Push(0)
	myStack.GetMin()
	myStack.Pop()
	myStack.GetMin()
}
