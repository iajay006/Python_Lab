
# WEEK 4: Working with tuples and sets

# Q1: Convert a list of tuples into a dictionary
def Question1():
    lst = [("a", 1), ("b", 2), ("c", 3)]
    d = dict(lst)
    print("Dictionary:", d)


# Q2a: Reverse a tuple
def Question2a():
    t = (1, 2, 3, 4, 5)
    print("Original tuple:", t)
    print("Reversed tuple:", t[::-1])


# Q2b: Swap two tuples
def Question2b():
    t1 = (1, 2, 3)
    t2 = (4, 5, 6)
    print("Before Swap:", t1, t2)
    t1, t2 = t2, t1
    print("After Swap:", t1, t2)


# Q3: Print value 20 and modify to 220
def Question3():
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
    print("Original tuple:", tuple1)
    print("Value:", tuple1[1][1])  # printing 20
    tuple1[1][1] = 220
    print("Modified tuple:", tuple1)


# Q4: Unpack tuple and count occurrence of 20
def Question4():
    tuple1 = (10, 20, 30, 20)
    a, b, c, d = tuple1
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("Count of 20:", tuple1.count(20))


# Q5: Add all elements of list into set
def Question5():
    sample_list = ["Blue", "Green", "Red"]
    sample_set = {"Yellow", "Orange", "Black"}
    sample_set.update(sample_list)
    print("Updated set:", sample_set)


# Q6: New set with identical items and unique items
def Question6():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    identical = set1 & set2
    unique = set1 ^ set2
    print("Identical items:", identical)
    print("Unique items:", unique)


# Q7: Remove items not common to both sets
def Question7():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.intersection_update(set2)
    print("Common items:", set1)


#call all questions
if __name__ == "__main__":
    print("\n--- Question 1 ---")
    Question1()
    print("\n--- Question 2a ---")
    Question2a()
    print("\n--- Question 2b ---")
    Question2b()
    print("\n--- Question 3 ---")
    Question3()
    print("\n--- Question 4 ---")
    Question4()
    print("\n--- Question 5 ---")
    Question5()
    print("\n--- Question 6 ---")
    Question6()
    print("\n--- Question 7 ---")
    Question7()
