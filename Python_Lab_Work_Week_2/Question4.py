def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Optional: ignore case and spaces
    return s == s[::-1]

user_input = input("Enter a string: ")
print("Is palindrome:", is_palindrome(user_input))
