def main():
    key = taqueria()

def taqueria():
    dict = {
        "Baja Taco":4.00,
        "Burrito":7.50,
        "Bowl":8.50,
        "Nachos":11.00,
        "Quesadilla":8.50,
        "Super Burrito":8.50,
        "Super Quesadilla":9.50,
        "Taco":3.00,
        "Tortilla Salad":8.00
    }
    total =0.00
    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            print("Total: $",total)
            break
        if item in dict:
            total = total + dict[item]
            print("Total: $",end="")
            print("{0:.2f}".format(total))
        else:
            pass
    return

main()