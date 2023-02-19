def main():
    Item = nutrition(input("Item: "))

def nutrition(n):
    d = {
        "apple" : 130,
        "Avocado":50,
        "banana":110,
        "Kiwifruit":90,
        "pear":100,
        "Sweet Cherries":100
    }
    if n in d:
        print("Calories: ", d[n])
    else:
        exit()
    return n

main()
