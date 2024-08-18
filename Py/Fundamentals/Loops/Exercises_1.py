# [Exercises: Level 1] Python Fundamentals - Loops

'''
Iterate 0 to 10 using for loop, do the same using while loop.

Iterate 10 to 0 using for loop, do the same using while loop.

Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

Use for loop to iterate from 0 to 100 and print only even numbers

Use for loop to iterate from 0 to 100 and print only odd numbers
'''

# Iterate 0 to 10 using for loop
print("For loop from 0 to 10:")
for i in range(11):
    print(i)

# Iterate 0 to 10 using while loop
print("\nWhile loop from 0 to 10:")
i = 0
while i <= 10:
    print(i)
    i += 1

# Iterate 10 to 0 using for loop
print("\nFor loop from 10 to 0:")
for i in range(10, -1, -1):
    print(i)

# Iterate 10 to 0 using while loop
print("\nWhile loop from 10 to 0:")
i = 10
while i >= 0:
    print(i)
    i -= 1

# Print triangle pattern
print("\nTriangle pattern:")
for i in range(1, 8):
    print('#' * i)

# Nested loops to create 8x8 grid pattern
print("\n8x8 grid pattern:")
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# Print multiplication pattern
print("\nMultiplication pattern:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# Iterate through the list and print items
print("\nIterate through list:")
items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in items:
    print(item)

# Print only even numbers from 0 to 100
print("\nEven numbers from 0 to 100:")
for i in range(101):
    if i % 2 == 0:
        print(i)

# Print only odd numbers from 0 to 100
print("\nOdd numbers from 0 to 100:")
for i in range(101):
    if i % 2 != 0:
        print(i)