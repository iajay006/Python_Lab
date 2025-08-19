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
Question5()
