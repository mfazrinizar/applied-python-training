# [Exercises: Level 3] Python Fundamentals - Conditionals

'''
Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Aurora',
    'last_name': 'Luna',
    'age': 6,
    'country': 'Indonesia',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Jl. Jalan',
        'zipcode': '123456'
    }
}
Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

If the person lives in Indonesia, print the information in the following format:

Aurora Luna lives in Indonesia.
'''

# Person dictionary
person = {
    'first_name': 'Aurora',
    'last_name': 'Luna',
    'age': 6,
    'country': 'Indonesia',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Jl. Jalan',
        'zipcode': '123456'
    }
}

# Check if the person dictionary has skills key
if 'skills' in person:
    skills = person['skills']
    
    # Print out the middle skill in the skills list
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])
    
    # Check if the person has 'Python' skill and print out the result
    if 'Python' in skills:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")
    
    # Determine the person's developer title based on their skills
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif set(skills) >= {'Node', 'Python', 'MongoDB'}:
        print("He is a backend developer")
    elif set(skills) >= {'React', 'Node', 'MongoDB'}:
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# Check if the person lives in Indonesia and print the information
if person['country'] == 'Indonesia':
    print(f"{person['first_name']} {person['last_name']} lives in Indonesia.")