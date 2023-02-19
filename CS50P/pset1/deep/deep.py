def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    x = x.strip().lower()
    x = deep(x)

def deep(d):
    # TODO
    if d == '42' or d == "forty-two" or d == 'forty two':
        print("YES")
    else:
        print('NO')
    return d

main()