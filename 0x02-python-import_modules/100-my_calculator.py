#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = 0

    match operator:
        case "+":
            result = calc.add(a, b)
        case "*":
            result = calc.mul(a, b)
        case "/":
            result = calc.div(a, b)
        case "-":
            result = calc.sub(a, b)
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

    print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
