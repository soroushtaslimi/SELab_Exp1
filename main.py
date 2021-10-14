# SELab experiment 1

def get_inputs():
    operand1, operator, operand2 = input("give me your hardest calculation problem: ").split()
    return operator, float(operand1), float(operand2)
