

# -------------- DATA STRUCTURES--------------

'''
stores multiple values. 
they r containers that include:

1: LISTS: like a shopping list []
2: DICTIONARIES: like a phone book {}
3: TUPLES : like coordinates (fixed values)()
4: SETS: like a bag of unique items.

'''















# --------- LISTS ---------

'''
basically,
a list is like this

list = ["alpha", "beta", "gamma", "theta"]   '''
#        [0,        1,      2,       3]
#        [-4,      -3,     -2,      -1]


#--------------------------


age = 17
has_license = False
my_list = ["Eman", 17, age, True,has_license]


my_list[0]
my_list[4]
my_list[2]

has_license = my_list[-1]
age = my_list[-2]


print(my_list[2])
#--------------------------



fruits = ["apple", "banana", "orange"]
# set items
print(fruits[0])   # apple
print(fruits[2])   # orange
print(fruits[1])   # banana
print(fruits[-1])  # orange
print(fruits[-2])  # banana
# slicing
print(fruits[0:2]) # ['apple', 'banana']
print(fruits[1:])  # ['banana', 'orange']

# we can also change an item in a list
fruits[0] = "mango"
print(fruits) # hence apple is replaced by mango

fruits.append("grape") 
fruits.insert(3, "kiwi") #insert at position
print(fruits)

# to remove
fruits.remove("grape")
print(fruits) # it will be modified now

# to remove and return last
last = fruits.pop()
print(fruits)

# remove by index
del fruits[0]
print(fruits) #therefore, it removes mango


#-----------------------------

# LIST METHODS :

numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))         # 6 (length)
print(numbers.count(1))     # 2 (count occurrences)
print(numbers.index(4))     # 2 (find position)

# Sorting
numbers.sort()              # Sort in place
print(numbers)              # [1, 1, 3, 4, 5, 9]

numbers.reverse()           # Reverse order
print(numbers)              # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()   # Create a copy


#-----------------------------
# CHECKING LISTS

fruits = ["apple", "banana", "orange"]

# Check if item exists
if "apple" in fruits:
    print("Found apple!")

# Check if list is empty
if fruits:
    print("List has items")
else:
    print("List is empty")















# --------- DICTIONARIES ---------
'''
Dictionaries
Store data with key-value pairs

Real-world examples:
Phone book: name > phone number
Menu: dish > price
User profile: username > user info

'''






#---Creating dictionaries---:-

# Empty dictionary
my_dict = {}

# Dictionary with data
person = {
    "name": "eman",
    "age": 17,
    "city": "New York"
}

# Different ways to create
scores = dict(math=95, english=87, urdu=92)






#-----Accessing values-----:-
person = {'name': 'eman', 'age': 17, 'city': 'New York'}

# Get values by key
print(person["name"])       # "eman"
print(person["age"])        # 17
print(person["city"])       # New York
# Safer with get()
print(person.get("job"))    # None (no error)
print(person.get("job", "Unknown"))  # "Unknown" (default)
print(person) #{'name': 'eman', 'age': 17, 'city': 'New York'}





#---Changing dictionaries--:-

person = {"name": "Eman", "age": 17}

#add or update
person["email"] = "eman@gmail.com"
person["age"] = 18 #updates existing age
#remove items
del person["email"]   #remove by key
age = person.pop("age")  #remove and return
person.clear()  # remove all items





#----Dictionary methods---:-


person = {"name": "eman", "age": 17, "city": "New York"}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['eman', 17, 'New York'])
print(person.items())   # dict_items([('name', 'eman'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 18, "job": "Engineer"})
print(person)




#----Nested dictionaries---:-

# Dictionary of dictionaries
students = {
    "eman": {"age": 17, "grade": "A"},
    "zayden": {"age": 21, "grade": "B"},
    "elisa": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["zayden"]["grade"])  # "B"





























# -------------- TUPLES ---------------
'''
Tuples
Store data in an ordered, immutable sequence

Use tuples for data that shouldn’t change:
Coordinates (x, y)
RGB colors (255, 0, 0)
Database records
Function return values

'''


#---Creating tuples---:-

# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (92,)  # Note the comma
not_tuple = (92)  # This is just 92 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20




#---Accessing items in tuples---:-

point = (1, 5)
colors = ("red", "green", "blue")
print(point[1])
print(colors[-1])

# Get items
print(point[0])      # 1
print(colors[-1])    # "blue"

# Slicing works too
print(colors[0:2])   # ("red", "green")




#---Tuple unpacking---:-

# Unpack values
point = (1, 5)
x, y = point  # x = 1, y = 5

xavier = ("lame", "dutch", "anaconda")
e,i,o = xavier  # e = "lame", i = "dutch", o = "anaconda"

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!
























# -------------- SETS ---------------
'''

Sets are collections that only store unique values.
They automatically remove duplicates.

LIKE:

A bag of unique marbles
Guest list (each person once)
Unique tags or categories


'''





#--- Creating sets ---:-
'''
You can create sets two ways:
with set() or with curly braces {} 
(but only when it has values).
'''

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}




#--- Basic operations ---:-

colors = {"red", "blue"}

# Add items
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}

# Remove items
colors.remove("blue")    # Error if not found
colors.discard("yellow") # No error if not found

# Check membership
if "red" in colors:
    print("Red is available")





#--- Common uses---:-

names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']


allowed_users = {"alice", "bob", "charlie"}
if "alice" in allowed_users:  # Very fast!
    print("Access granted")




    