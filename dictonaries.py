# Dictionaries
# Overview:
# A dictionary in Python is a data structure that allows you to store and retrieve values using keys. It is also known as a hashmap or associative array in other programming languages. Dictionaries are implemented as hash tables, providing fast access to values based on their keys.

# Creating a Dictionary:
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name']) 
my_dict['age'] = 26  # Modifying a value
my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
if 'age' in my_dict:
    print('Age is present in the dictionary')
for key, value in my_dict.items():
    print(key, value)