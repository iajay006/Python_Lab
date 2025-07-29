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
