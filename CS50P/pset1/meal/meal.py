def main():
    T = input("What time is it? ")
    T = convert(T)


def convert(time):
    hours, minutes = time.split(":")
    if hours == "7":
        print("breakfast time")
    elif hours == "13":
        print("lunch time")
    elif hours == "18":
        print("dinner time")
    else:
        exit()


if __name__ == "__main__":
    main()

