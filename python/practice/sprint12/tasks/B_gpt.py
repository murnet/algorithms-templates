class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


def is_operator(token):
    return token in "+-*/"


def apply_operator(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 // operand2
    else:
        raise ValueError("Invalid operator: " + operator)


def rpn_calculator(expression):
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.push(int(token))
        elif is_operator(token):
            if stack.size() < 2:
                raise ValueError("Not enough operands for operator: " + token)
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(token, operand1, operand2)
            stack.push(result)
        else:
            raise ValueError("Invalid token: " + token)

    if stack.size() != 1:
        raise ValueError("Invalid expression")

    return stack.peek()


if __name__ == "__main__":
    while True:
        try:
            expression = input("Enter an RPN expression (space-separated): ")
            if expression.lower() in ["exit", "quit"]:
                break
            result = rpn_calculator(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
