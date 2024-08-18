# [Exercises: Level 2] Python Fundamentals - Functions

'''
Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

Call your function is_empty, it takes a parameter and it checks if it is empty or not

Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation). m
'''

# 1. Function to count evens and odds in a number
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}. The number of evens are {evens}."

# 2. Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 3. Function to check if a parameter is empty
def is_empty(param):
    return not bool(param)

# 4. Function to calculate mean
def calculate_mean(lst):
    return sum(lst) / len(lst)

# 5. Function to calculate median
def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

# 6. Function to calculate mode
def calculate_mode(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    max_count = max(count.values())
    mode = [k for k, v in count.items() if v == max_count]
    return mode

# 7. Function to calculate range
def calculate_range(lst):
    return max(lst) - min(lst)

# 8. Function to calculate variance
def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

# 9. Function to calculate standard deviation
def calculate_std(lst):
    variance = calculate_variance(lst)
    return variance ** 0.5

# Testing the functions
print(evens_and_odds(100))  # The number of odds are 50. The number of evens are 51.
print(factorial(5))  # 120
print(is_empty([]))  # True
print(is_empty([1, 2, 3]))  # False
print(calculate_mean([1, 2, 3, 4, 5]))  # 3.0
print(calculate_median([1, 2, 3, 4, 5]))  # 3
print(calculate_mode([1, 2, 2, 3, 4]))  # [2]
print(calculate_range([1, 2, 3, 4, 5]))  # 4
print(calculate_variance([1, 2, 3, 4, 5]))  # 2.0
print(calculate_std([1, 2, 3, 4, 5]))  # 1.4142135623730951