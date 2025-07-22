#Question 3 :

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter value of n: "))
print("Fibonacci series:")
fibonacci(n)

print("Factorial of", n, "is:", factorial(n))
