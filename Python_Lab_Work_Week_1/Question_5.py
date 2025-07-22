#Question :

def square_n_numbers(n):
    for i in range(1, n + 1):
        print(f"{i}^2 = {i*i}")

n = int(input("Enter n: "))
square_n_numbers(n)
