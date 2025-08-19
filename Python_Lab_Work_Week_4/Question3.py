def Question3():
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
    print("Original tuple:", tuple1)
    print("Value:", tuple1[1][1])  # printing 20
    tuple1[1][1] = 220
    print("Modified tuple:", tuple1)
Question3()
