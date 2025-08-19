def Question6():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    identical = set1 & set2
    unique = set1 ^ set2
    print("Identical items:", identical)
    print("Unique items:", unique)
Question6()
