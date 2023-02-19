def main():
    x = vowel(input("Input: "))  # Take input
    print(x)             # Print output

def vowel(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    return result

main()
