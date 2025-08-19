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
Question1()
