def main():
    m = einstein(input("m: "))              #Take input
    print('E: ', m)                         # Print output

def einstein(E):
    m = int(E)
    c = 300000000             #Give value of c
    E = m*c**2                #Give equation
    return E                                               #return function

main()