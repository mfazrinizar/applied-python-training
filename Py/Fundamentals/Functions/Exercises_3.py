# [Exercises: Level 3] Python Fundamentals - Functions

'''
Write a function called is_prime, which checks if a number is prime.

Write a functions which checks if all items are unique in the list.

Write a function which checks if all the items of the list are of the same data type.
'''

# 1. Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. Function to check if all items in a list are unique
def are_all_items_unique(lst):
    return len(lst) == len(set(lst))

# 3. Function to check if all items in a list are of the same data type
def are_all_items_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)

# Testing the functions
print(is_prime(7))  # True
print(is_prime(10))  # False
print(are_all_items_unique([1, 2, 3, 4, 5]))  # True
print(are_all_items_unique([1, 2, 2, 3, 4]))  # False
print(are_all_items_same_type([1, 2, 3, 4, 5]))  # True
print(are_all_items_same_type([1, '2', 3, 4, 5]))  # False