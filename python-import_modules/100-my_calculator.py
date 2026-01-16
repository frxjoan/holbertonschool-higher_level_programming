#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == chr(42):
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        return 1

    print("{} {} {} = {}".format(a, op, b, result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
