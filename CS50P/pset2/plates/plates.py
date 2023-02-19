def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #TODO
    numbers = ('0','1','2','3','4','5','6','7','8','9')
    if len(s) < 7:
        if s[:1] not in numbers:
            if s[2] != '0':
                if s[1] != '-':
                    return True
    else:
        return False

main()