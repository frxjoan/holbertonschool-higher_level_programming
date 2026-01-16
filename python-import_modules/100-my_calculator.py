#!/usr/bin/python3
import sys
import calculator_1

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    result = 0

    ops = {
        "+": calculator_1.add,
        "-": calculator_1.sub,
        chr(42): calculator_1.mul,
        "/": calculator_1.div,
    }

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = ops[op](a, b)
    print("{} {} {} = {}".format(a, op, b, result))
