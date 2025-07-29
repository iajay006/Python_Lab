def Question1():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    
    n = int(input("Enter a number for factorial: "))
    print("Factorial is:", factorial(n))


def Question2():
    def sum_all(*args):
        return sum(args)
    
    nums = input("Enter numbers separated by spaces to sum: ").split()
    nums = [int(x) for x in nums]
    print("Sum is:", sum_all(*nums))


def Question3():
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


def Question4():
    def is_palindrome(s):
        s = s.lower().replace(" ", "")  # Optional: ignore case and spaces
        return s == s[::-1]

    user_input = input("Enter a string: ")
    print("Is palindrome:", is_palindrome(user_input))


def Question5():
    def custom_length(s):
        count = 0
        for i in s:
            count += 1
        return count

    def print_right_aligned(s, width=80):
        length = custom_length(s)
        output = str(length) + s
        print(output.rjust(width))

    user_input = input("Enter a string: ")
    print_right_aligned(user_input)


# Call each question function
Question1()
Question2()
Question3()
Question4()
Question5()
