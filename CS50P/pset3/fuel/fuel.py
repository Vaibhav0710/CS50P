def main():
    x = get_int()
    x = fuel(x)

def get_int():
    while True:
        try:
            z = input("Fraction: ")
            a,b = z.split("/")
            a = int(a)
            b = int(b)
            if a == int(a):
                if a < b or a == b:
                    True
                    return z
            else:
                False
        except (ValueError, ZeroDivisionError):
            pass

def fuel(f):
    v,w = f.split("/")
    v = int(v)
    w = int(w)
    g = v/w
    if g >= 0.85:
        print("F")
    elif g >= 0.65:
        print("75%")
    elif g >= 0.40:
        print("50%")
    elif g >= 0.15:
        print("25%")
    else:
        print("E")

    return f

main()