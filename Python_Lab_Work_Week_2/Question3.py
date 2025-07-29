def process_string(s):
    # Count characters
    length = len(s)

    # Reverse string
    reversed_string = s[::-1]

    # Display results
    print("Original String:", s)
    print("Number of characters:", length)
    print("Reversed String:", reversed_string)

user_input = input("Enter a string: ")
process_string(user_input)

