def main():
    print("Amount Due: 50")
    x = int(input("Insert Coin: "))
    x = Coke(x)

def Coke(c):
    machine = 50
    while machine >= 0:
        if machine == 0:
            print("Change Owed: 0")
            exit()
        elif c == 25:
            machine = machine - c
            if machine == 0:
                continue
            elif machine > 0:
                print("Amount Due: ", machine)
                c = int(input("Insert Coin: "))

            else:
                print("Change own: ", -machine)
                continue
        elif c == 10:
            machine = machine - c
            if machine == 0:
                continue
            elif machine > 0:
                print("Amount Due: ", machine)
                c = int(input("Insert Coin: "))
            else:
                print("Change own: ", -machine)
                continue
        elif c == 5:
            machine = machine - c
            if machine == 0:
                continue
            elif machine > 0:
                print("Amount Due: ", machine)
                c = int(input("Insert Coin: "))
            else:
                print("Change own: ", -machine)
                continue
        else:
            print("Amount Due: ", machine)
            c = int(input("Insert Coin: "))
    return c
main()
