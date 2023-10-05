#!/usr/bin/python3

if __name__ == "__main__":
    """Handle some basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    opers = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(opers.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, opers[sys.argv[2]](a, b)))
