def Question1():
    num1=eval(input("Enter two number: "))
    num2=eval(input("Enter two number: "))
    sum=num1+num2
    print("Sum is: ",sum)
    diff=num1-num2
    print("Difference is: ",diff)
    multiple=num1*num2
    print("Multiple is: ",multiple)
    division=num1/num2
    print("Division is: ",division)


def Question2():
    P = eval(input("Enter Principal amount (P): "))
    T = eval(input("Enter Time in years (T): "))
    R = eval(input("Enter Rate of Interest (R): "))

    SI = (P * T * R) / 100
    print("Simple Interest =", SI)


def Question3():
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


def Question4():
    distance_km = 10
    time_minutes = 43
    time_seconds = 30

    # Convert total time into hours
    total_time_hours = (time_minutes + time_seconds / 60) / 60

    # Convert kilometers to miles
    distance_miles = distance_km / 1.61

    # Average speed (miles/hour)
    average_speed = distance_miles / total_time_hours

    # Average time per mile
    average_time_per_mile = total_time_hours / distance_miles * 60  # in minutes

    print("Average speed (miles/hour):", round(average_speed, 2))
    print("Average time per mile (minutes):", round(average_time_per_mile, 2))


def Question5():
    def square_n_numbers(n):
        for i in range(1, n + 1):
            print(f"{i}^2 = {i*i}")

    n = int(input("Enter n: "))
    square_n_numbers(n)
    
Question1()
Question2()
Question3()
#Question4()
#Question5()


