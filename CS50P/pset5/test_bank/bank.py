def main():
    x = input("Greeting: ")
    x = x.strip().lower()
    x = value(x)

def value(h):
    #TODO
    if 'hello' in h:
        print("$0")
    elif h[0] == "h":
        print("$20")
    else:
        print('$100')
    return h

main()

