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
Question4()
