#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if (op == '+'):
        ans = add(a, b)
    elif (op == '-'):
        ans = sub(a, b)
    elif (op == '*'):
        ans = mul(a, b)
    elif (op == '/'):
        if (b == 0):
            sys.exit(1)
        ans = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} + {} = {}".format(a, b, ans))
