This code implements a stack data structure to create a simple text-based calculator that can evaluate expressions with parentheses.

This mini-project demonstrates the use of a stack to evaluate a mathematical expression with parentheses. It uses a simple stack implementation with basic push, pop, and peek operations. The evaluate_expression function reads an expression containing numbers and parentheses, calculates the result by considering the parentheses, and prints the final result. This is a basic example to introduce you to the concept of stacks in the context of a simple calculator.



Stack Class:

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")
The Stack class defines a basic stack data structure with three main methods: push, pop, and peek.
The push method adds an item to the top of the stack.
The pop method removes and returns the item from the top of the stack.
The peek method returns the item from the top of the stack without removing it.
The is_empty method checks if the stack is empty.

evaluate_expression Function:

def evaluate_expression(expression):
    stack = Stack()

    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        elif char == '(':
            stack.push(char)
        elif char == ')' and not stack.is_empty() and stack.peek() == '(':
            stack.pop()
            result = 0
            while not stack.is_empty() and stack.peek().isdigit():
                result += stack.pop()
            stack.push(result)
        else:
            raise ValueError("Invalid expression")

    final_result = 0
    while not stack.is_empty():
        final_result += stack.pop()

    return final_result
The evaluate_expression function takes a mathematical expression as input.
It uses a stack to evaluate the expression by considering the parentheses.
It iterates through each character in the expression.
If the character is a digit, it is pushed onto the stack.
If the character is an opening parenthesis '(', it is pushed onto the stack.
If the character is a closing parenthesis ')' and the top of the stack is an opening parenthesis '(', it calculates the result inside the parentheses and pushes it back onto the stack.
If the character is neither a digit nor a valid parenthesis, it raises a ValueError for an invalid expression.
After processing the entire expression, it calculates the final result by summing up the values remaining on the stack.


main Function:

def main():
    expression = input("Enter a mathematical expression with parentheses: ")
    
    try:
        result = evaluate_expression(expression)
        print(f"Result of the expression: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
The main function takes user input for a mathematical expression.
It then attempts to evaluate the expression using the evaluate_expression function.
If successful, it prints the result; otherwise, it catches and prints any ValueError raised during the evaluation.

This code provides a simple example of using a stack to handle parentheses in a mathematical expression, making it a basic calculator that can calculate expressions like "(2+3)+4".
