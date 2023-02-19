def main():
    x = lower_the_text(input("Enter the text: "))          #Take input
    print(x)                                               #print output


def lower_the_text(l):
    l=l.lower()          #lower the input value
    return l

main()