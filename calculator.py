import sys

USAGE = """Usage: python3 calculator.py <operation> <num1> <num2>

<operation> can be add, sub, mul, div
"""

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

OPERATIONS = {
    'add': add,
    'sub': sub,
    'mul': mul,
    'div': div,
}

def main(args):
    if len(args) != 3 or args[0] not in OPERATIONS:
        print(USAGE)
        return 1
    op_name = args[0]
    try:
        num1 = float(args[1])
        num2 = float(args[2])
    except ValueError:
        print("Numbers must be valid numeric values")
        return 1
    try:
        result = OPERATIONS[op_name](num1, num2)
    except Exception as e:
        print(e)
        return 1
    print(result)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
