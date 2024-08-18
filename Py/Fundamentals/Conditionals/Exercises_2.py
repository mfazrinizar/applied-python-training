# [Exercises: Level 2] Python Fundamentals - Conditionals

'''
Write a code which gives grade to students according to theirs scores:
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''
def assign_grade(score):
    if 80 <= score <= 100:
        return 'A'
    elif 70 <= score <= 79:
        return 'B'
    elif 60 <= score <= 69:
        return 'C'
    elif 50 <= score <= 59:
        return 'D'
    elif 0 <= score <= 49:
        return 'F'
    else:
        return 'Invalid score'

'''
Check if the season is Autumn, Winter, Spring or Summer. 
If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. 
March, April or May, the season is Spring June, July or August, the season is Summer.
'''
def determine_season(month):
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

'''
The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
'''
def check_and_add_fruit(fruit, fruits_list):
    fruit = fruit.lower()
    if fruit in fruits_list:
        print('That fruit already exists in the list')
    else:
        fruits_list.append(fruit)
        print('Modified list:', fruits_list)

# Test the assign_grade function
score = int(input("Enter the score: ")) # input: 86
print("Grade:", assign_grade(score))

print()

# Test the determine_season function
month = input("Enter the month: ") # input: September
print("Season:", determine_season(month)) 

print()

# Test the check_and_add_fruit function
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ") # input: orange
check_and_add_fruit(fruit, fruits)