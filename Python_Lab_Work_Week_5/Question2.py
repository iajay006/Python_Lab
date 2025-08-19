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
