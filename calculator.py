"""A small command-line calculator used to practise Git branching and merging."""

import sys


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b."""
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a, op, b):
    """Apply the operator op to the numbers a and b."""
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {op}")
    return OPERATIONS[op](a, b)


def main(argv):
    if len(argv) != 4:
        print("Usage: python calculator.py <number> <operator> <number>")
        print("Example: python calculator.py 8 / 2")
        return 1
    a, op, b = float(argv[1]), argv[2], float(argv[3])
    print(calculate(a, op, b))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
