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


def main():
    expression = input("Enter a mathematical expression with parentheses: ")
    
    try:
        result = evaluate_expression(expression)
        print(f"Result of the expression: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
