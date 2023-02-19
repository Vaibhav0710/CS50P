def main():
    x = face(input("Text: "))  # Take input
    print(x)             # Print output

def face(f):
    f = f.replace(":)", "🙂").replace(":(", "🙁")         #replacement
    return f                                               #return function

main()
