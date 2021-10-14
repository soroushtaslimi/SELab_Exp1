# SELab experiment 1

def get_inputs():
    operand1, operator, operand2 = input("give me your hardest calculation problem: ").split()
    return operator, float(operand1), float(operand2)


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a / b


def calculate(oprator, operand1, operand2):
    if operator == '+':
        return add(operand1, operand2)
    elif operator == '-':
        return minus(operand1, operand2)
    elif operator == '*':
        return multiply(operand1, operand2)
    elif operator == '/':
        return divide(operand1, operand2)
    


if __name__ == '__main__':
    operator, operand1, operand2 = get_inputs()
    res = calculate(operator, operand1, operand2)
    print(res);
