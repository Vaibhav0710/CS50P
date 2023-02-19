def main():
    x = playback(input("Text: "))  # Take input
    print(x)             # Print output

def playback(p):
    p = p.replace(" ", "   ")         #replacement
    return p                          #return function

main()