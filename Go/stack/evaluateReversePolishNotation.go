package stack

import (
	"fmt"
	"strconv"
)

type myStack []string

func (s *myStack) push(char string) {
	(*s) = append(*s, char)
}

func (s *myStack) pop() string {
	top := (*s)[len(*s)-1]
	(*s) = (*s)[:len(*s)-1]
	return top
}

func evalRPN(tokens []string) int {
	s := myStack{}
	for _, char := range tokens {
		if !isOperator(char) {
			s.push(char)
			continue
		}

		secondOperand := s.pop()
		firstOperand := s.pop()

		s.push(operate(firstOperand, secondOperand, char))
	}

	result, _ := strconv.Atoi(s.pop())
	return result
}

func operate(operand1, operan2, operator string) string {
	temp1, _ := strconv.Atoi(operand1)
	temp2, _ := strconv.Atoi(operan2)

	switch operator {
	case "+":
		return fmt.Sprintf("%d", (temp1 + temp2))
	case "*":
		return fmt.Sprintf("%d", (temp1 * temp2))
	case "-":
		return fmt.Sprintf("%d", (temp1 - temp2))
	case "/":
		return fmt.Sprintf("%d", (temp1 / temp2))
	}

	return ""
}

func isOperator(char string) bool {
	return (char == "+" || char == "*" || char == "-" || char == "/")
}
