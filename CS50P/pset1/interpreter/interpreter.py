def main():
    expression = input("Expression: ")
    expression = math(expression)


def math(m):
    # TODO
    x, y, z = m.split()
    x = float(x)
    z = float(z)
    if y == "+":
        print(x+z)
    elif y == "-":
        print(x-z)
    elif y == "/":
        print(x / z)
    elif y == '*':
        print(x * z)
    else:
        print("try again")

    return m


main()
