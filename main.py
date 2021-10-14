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


if __name__ == '__main__':
    operator, operand1, operand2 = get_inputs()

