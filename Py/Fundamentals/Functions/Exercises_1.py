# [Exercises: Level 1] Python Fundamentals - Functions

'''
Exercises: Level 1
Declare a function add_two_numbers. It takes two parameters and it returns a sum.

Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

Write a function called calculate_slope which return the slope of a linear equation

Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
'''

import math

# 1. Function to add two numbers
def add_two_numbers(a, b):
    return a + b

# 2. Function to calculate the area of a circle
def area_of_circle(r):
    return math.pi * r * r

# 3. Function to add all numbers
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return "All items must be numbers"

# 4. Function to convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 5. Function to check the season
def check_season(month):
    month = month.capitalize()
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid month'

# 6. Function to calculate the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# 7. Function to solve a quadratic equation
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"

# 8. Function to print each element of a list
def print_list(lst):
    for item in lst:
        print(item)

# 9. Function to reverse a list
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# 10. Function to capitalize list items
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# 11. Function to add an item to a list
def add_item(lst, item):
    lst.append(item)
    return lst

# 12. Function to remove an item from a list
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 13. Function to sum all numbers in a range
def sum_of_numbers(n):
    return sum(range(n + 1))

# 14. Function to sum all odd numbers in a range
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# 15. Function to sum all even numbers in a range
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

# Testing the functions
print(add_two_numbers(3, 4))  # 7
print(area_of_circle(5))  # 78.53981633974483
print(add_all_nums(1, 2, 3, 4))  # 10
print(add_all_nums(1, '2', 3))  # All items must be numbers
print(convert_celsius_to_fahrenheit(30))  # 86.0
print(check_season('March'))  # Spring
print(calculate_slope(1, 2, 3, 4))  # 1.0
print(solve_quadratic_eqn(1, -3, 2))  # (2.0, 1.0)
print_list(['a', 'b', 'c'])  # a b c
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
print(capitalize_list_items(['apple', 'banana']))  # ['Apple', 'Banana']
print(add_item([1, 2, 3], 4))  # [1, 2, 3, 4]
print(remove_item([1, 2, 3], 2))  # [1, 3]
print(sum_of_numbers(5))  # 15
print(sum_of_odds(5))  # 9
print(sum_of_even(5))  # 6