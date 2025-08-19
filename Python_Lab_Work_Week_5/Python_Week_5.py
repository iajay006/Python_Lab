# WEEK 5: Working with Dictionaries

# Q1: Convert two lists into a dictionary
def Question1():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    my_dict = {}
    my_dict.update(dict(zip(keys, values)))
    print("Q1 Dictionary:", my_dict)
    print("Sorted Keys with Values:")
    for k in sorted(my_dict.keys()):
        print(k, ":", my_dict[k])
    print()

def Question2():
    my_dict = {'a': 1, 'b': 2}
    print("Original:", my_dict)

    # Insert 'c':3 between 'a' and 'b'
    new_dict = {}
    for key, value in my_dict.items():
        new_dict[key] = value
        if key == 'a':
            new_dict['c'] = 3

    print("After Insertion:", new_dict)

    # Delete 'b'
    del new_dict['b']
    print("After Deletion:", new_dict)
    print()

Question2()

# Q3: Check if value exists
def Question3():
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    if 200 in sample_dict.values():
        print("Q3: 200 exists in dictionary")
    else:
        print("Q3: 200 does not exist")
    print()

# Q4: Rename key city → location
def Question4():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    print("Before:", sample_dict)
    sample_dict['location'] = sample_dict.pop('city')
    print("After:", sample_dict)
    print()

# Q5: Change Brad’s salary to 8500
def Question5():
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }
    print("Before:", sample_dict)
    for key, val in sample_dict.items():
        if val['name'] == 'Brad':
            val['salary'] = 8500
    print("After:", sample_dict)
    print()


#call all questions
if __name__ == "__main__":
    print("\n--- Question 1 ---")
    Question1()
    print("\n--- Question 2 ---")
    Question2()
    print("\n--- Question 3 ---")
    Question3()
    print("\n--- Question 4 ---")
    Question4()
    print("\n--- Question 5 ---")
    Question5()

