# Add dictionary
grocery = {}

# Loop
while True:
    # Try & Except
    try:
        # input
        item = input()

        # Check if item is already in the dictionary
        if item.lower() in grocery:
            # if it's in then add 1 to the count
            grocery[item.lower()] += 1
        # if it's not in then add it for the first time
        else:
            grocery[item.lower()] = 1

    except EOFError:
        # Print all item in alphabetical order
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        # Stop the loop
        break