class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        """Return the last item from the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self.items)


def evaluate_expression(expression):
    stack = Stack()
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token == '(':
            stack.push(token)
        elif token == ')':
            subexpression = []
            while stack.peek() != '(':
                subexpression.insert(0, stack.pop())
            stack.pop()  # Remove '('
            result = evaluate_subexpression(subexpression)
            stack.push(result)
        else:
            stack.push(token)

    return int(stack.pop())


def evaluate_subexpression(subexpression):
    operator = subexpression.pop(0)
    result = int(subexpression.pop(0))

    while subexpression:
        operand = int(subexpression.pop(0))
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            if operand != 0:
                result /= operand
            else:
                raise ValueError("Division by zero")

    return result


if __name__ == "__main__":
    import sys

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python ex1.py '<expression>'")
        sys.exit(1)

    # Get the expression from the command line argument
    expression = sys.argv[1]
    
    # Evaluate the expression and print the result
    try:
        result = evaluate_expression(expression)
        print("Result of the expression:", result)
    except Exception as e:
        print("Error evaluating the expression:", e)
