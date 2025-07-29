def sum_all(*args):
    return sum(args)
    
nums = input("Enter numbers separated by spaces to sum: ").split()
nums = [int(x) for x in nums]
print("Sum is:", sum_all(*nums))
