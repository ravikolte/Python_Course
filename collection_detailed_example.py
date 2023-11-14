"""1. List:
A dynamic array that can store elements of different types.
python"""
my_list = [1, 2, 3, 4, 5]

# Built-in functions
print(len(my_list))           # Length of the list
print(my_list[2])             # Access element by index
my_list.append(6)             # Add element to the end
my_list.insert(2, 7)           # Insert element at index
my_list.remove(4)              # Remove element by value
popped_element = my_list.pop() # Remove and return last element


"""2. Tuple:
An ordered, immutable collection.
python
"""
my_tuple = (1, 2, 'a', 'b')

# Built-in functions
print(len(my_tuple))           # Length of the tuple
print(my_tuple[2])             # Access element by index



"""3. Set:
An unordered collection of unique elements.
python
"""
my_set = {1, 2, 3, 3, 3}

# Built-in functions
print(len(my_set))           # Number of unique elements
my_set.add(4)                 # Add element to the set
my_set.remove(2)              # Remove element by value



"""4. Dictionary:
A collection of key-value pairs.
python
"""
my_dict = {'one': 1, 'two': 2, 'three': 3}

# Built-in functions
print(len(my_dict))           # Number of key-value pairs
print(my_dict['two'])         # Access value by key
my_dict['four'] = 4           # Add new key-value pair
del my_dict['three']           # Remove key-value pair


"""5. String:
A sequence of characters.
python
"""
my_string = "Hello, Python!"

# Built-in functions
print(len(my_string))         # Length of the string
print(my_string[7])           # Access character by index
print(my_string.upper())      # Convert to uppercase
print(my_string.split(', '))  # Split into a list



"""6. Range:
A sequence of numbers.
python
"""
my_range = range(5)

# Built-in functions
print(len(my_range))          # Number of elements in the range
print(list(my_range))         # Convert range to a list
#These are just a few examples of the built-in functions for each collection type in Python.