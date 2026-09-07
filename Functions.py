'''

Functions:
Create reusable blocks of code


Building with functions:
Functions are reusable blocks of code that 
do specific tasks. Instead of writing the 
same code multiple times, you write it once
as a function and call it whenever needed.

Use:
> Don't repeat yourself
> Stay organized
> Fix bugs easier
> Test your code

Topics:

> DEFINING FUCTIONS
> PARAMETERS AND ARGUMENTS
> RETURNING VALUES

'''



#----------------- DEFINING FUNCTIONS -----------------



def greet():
    print("hello!!") # wont execute it rn
    print("hi") #we can also add more
    
greet()  # now it will execute the function


#--Naming functions--:-
'''
> use lowercase letters
> separate words with underscores
> be descriptive about what it does

'''
# good names:
def calculate_total():
    pass
def send_email():
    pass
def validate_password():
    pass

# bad names
def funcl():     #not descriptive
    pass
def Calculate(): #should be lowercase
    pass







#--Calling functions--:-

def say_goodbye():
    print("Goodbye!")
    print("see ya later!")

# Call it multiple times
say_goodbye()
say_goodbye()
say_goodbye()


def greet(students):
    print("Hello, " + students + "! Welcome.")
    print("We are glad to have you here.")
greet("Ali")
greet("Sara")
greet("Zain")
greet("Emaan")
greet("Bilal")

def invite(guests):
    print("You are invited, " + guests + "!")
    print(" Please join us for the event.")
invite("Ali")
invite("Sara")
invite("Zain")
invite("Emaan")
invite("Zayden")




def absentee(student):
    print("dear parents" + " your child "
          + student + " is absent today.")

absentee("Eman")
absentee("zayden")
absentee("Jade")
absentee("Aiden")






#---Functions with logic--:-

def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

# Use the function
check_weather()


def check_weather2():
    temperature2 = 12
    if temperature2 < 15:
        print("Grab a hot chocolate!")
    else:
        print("Enjoy the sunshine!")
check_weather2()  # Grab a hot chocolate!




#---Variable scope: Local vs Global--:-

#Local variables:
def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total price: {price+tax}")


calculate_price()  # Total price: 110

# This fails - price doesn't exist outside the function
#print(price)  # NameError: name 'price' is not defined

def calculate_marks():
    marks = 280
    negative_marking = marks * (-0.1)
    print(f"final marks: {marks + negative_marking}")


calculate_marks()  # final marks: 252.0





#Global variables:
discount_rate = 0.15  # Global variable

def apply_discount(price):
    discount = price * discount_rate  # Can read global variable
    return price - discount

result = apply_discount(100)
print(result)  # 85.0

















#-------------------- PARAMETERS---------------------

'''
Parameters let you pass data into functions.
Instead of hardcoding values, you make functions
flexible to work with different inputs.
'''




# Without parameters (inflexible)
def invite_kane():
    print("You are invited, Kane!")

# With parameters (flexible)
def invite_guest(name):
    print(f"hello {name}, you are invited!")

# Now it works for anyone
invite_guest("Eman")
invite_guest("Zayden")
invite_guest("kane")





#-----basic parameters-----:

def student_info(name, age):
    print(f"This is {name}, and they are {age} years old.")

student_info("eman", 17)
student_info("zayden", 19)
student_info("kane", 18)





#-----multiple parameters-----:

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

# Order matters!
calculate_total(100, 0.08, 10)  # $98





#-----Default values-----:

def greet(name, greeting="Hiiiiiiii"):
    print(f"{greeting}, {name}!")

# Use default
greet("Eman")           # Hiiiiiiii, Eman!

# Override default
greet("Zay", "Hiiiiiiii")       # Hiiiiiiii, Zay!
greet("jayden", "Hiiiiiiiii")  # Hiiiiiiiii, jayden!






#-----Keyword arguments-----:

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments (order matters)
create_profile("Zay", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Zay")
create_profile(name="Bob", city="LA", age=30)

























#-------------------- Return Values--------------------

# This function only prints
def add_print(a, b):
    print(a + b)

# without return:
def add_print(a, b):
    print(a + b)
add_print(a = 5, b = 3)  # Output: 8

# This function returns a value
def add_return(a, b):
    return a + b

# Now you can use the result
result = add_return(5, 3)
print(f"The result is {result}")  # The result is 8
print(f"the result is {result} fyi,btw...lol ml")



#-----The return statement-----:-
def calculate_area(width, height):
    area = width * height
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft



#-----Using returned values-----:-
def double(number):
    return number * 2

# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)  # 10 + 6 = 16

# Pass to other functions
print(double(10))  # 20

# Use in conditions
if double(7) > 10:
    print("Large number!")




#-----Returning multiple values-----:-
def get_min_max(numbers):
    return min(numbers), max(numbers)

# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)  # (1, 9)