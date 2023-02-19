from re import sub

def main():
    c = snake_case(input("camelCase: "))
    print("snakeCase: ", c)

def snake_case(s):
    for c in s:
        print(c, end="")
    return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()

main()
