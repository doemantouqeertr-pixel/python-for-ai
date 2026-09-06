


#DATA TYPES
'''
datatypes are different kind of information in python to be 
printed and python have 4 main data types 
1- numbers : for counting and calculations   #numbers
2- text : for words and messages             #strings
3- true/false : for decisions                #booleans
'''




# 1 - NUMBERS
'''
there are kinda 2 types of numbers

1 - integers [whole numbers without decimals]
    age = 25
    score = -10

2 - floats [numbers with decimal points]
    price = 19.99
    temperature = -5.3
    pi = 3.14159

forexample '''

total = 30 - 4
power = 90 * 3

print(power)
print(total)
print(power,total)
print(power+total)










# 2 - STRINGS
''' 
strings can be printed/created by 3 ways
1 - single quotes 
    eg : first = 'Python'
2 - double quotes
    eg : second = "Python"
3 - triple line quotes for multiple lines
    eg : paragraph = """ This
                         is a 
                        multiline string """ 

'''


"""-----------------------------------"""
string = "eman"
print(string)    #now we r using variable of 'string' that stored 'eman'

string_i_gotta_print = "emyyy"
print(string_i_gotta_print) #now we r using variable of 'string_i_gotta_print'
                            #that stored 'emyy'


"""-----------------------------------"""
string = "my name is eman touqeer"
first_name = "Eman"
last_name = "Touqeer" 
full_name = first_name + " " + last_name   #to print first and last name together
long_dash = "-" * 11    #to print a long dash 30 times

print(full_name)
print(long_dash)

print(len(full_name))   #we use 'len' to know/print the length





long_dash = "-" * 56
print(long_dash)











# 3 - BOOLEANS
 

'''
Booleans are the simplest data type,
they can only be True or False

is_logged_in = True
is_admin = False
has_permission = True


'''









'''---------------VALUES----------------'''
print(True)
print(False)


'''--------------FUNCTIONS---------------'''

'''------[bool()]--------'''
print(type(True))     #<class 'bool'>
print(bool(123))      #True
print(bool("hi"))     #True
print(bool())         #False
print(bool(0))        #False
print(bool(""))       #False
print(bool(None))     #False


'''-------[any()]--------'''

email = "amtrtt@gmail.com"
phone = "098-12337698"
username = "dotremant" 
print(any([email, phone, username])) #True,True,True 
#allows registration if any field is filled
#hence outcome will be True

email = "amtrtt@gmail.com"
phone = "098-12337698"
username = "" 
print(any([email, phone, username])) #True,True,False
#allows registration if any field is filled
#hence outcome will be True

email = ""
phone = "098-12337698"
username = "" 
print(any([email, phone, username])) #False,True,False 
#allows registration if any field is filled
#hence outcome will be True


'''-------[all()]--------'''

email = ""
phone = ""
username = ""
print(all([email, phone, username])) #False,False,False 
#Allows registration
#only if ALL fields is filled


'''----[isinstance()]----'''

print(isinstance(123, int))   #True bcz 123 is an integer
print(isinstance(True, str))  #False bcz 'True' ain't a string

print("Hello" .endswith("o") ) #True bcz 'Hello" do ends with "o"





'''-----------COMPARISON OPERATORS------------'''
'''
3 > 2 #[True]       # > means greater than
"x" < 2  #[False]    # < means less than
2-1 != 2  #[True]    # ! means 'not' & != means not equal to
len("Hi") == 3  #[False] # '==' compares while '=' means equal to
'''

'''--------'''
print(10==10) #sayin if 10 is equal to 10, hence 'True'
print(10!=10) #sayin if 10 isn't equal to 10, hence 'False'
print(7 > 3)  #True bcz 7 is greater than 3
print(7 >= 3) #True bcz 7 is greater than 3
print(3 < 8)  #True bcz 3 is smaller than 8
print(7 <= 7) #True bcz 7 is equal to 7
print(1 < 5 < 6) #hence everything is True, therefore its 'True"
print(5 > 4 < 6) #since one is False, henace its 'False'

'''-------'''
print("a" == "a") #strings can be compared too, Hence 'True'
print("A" == "a") #"A" & "a" both are different values, 'False'

'''-------'''

#to check if a value is between two bounds [chained comparisons]
#Is age between 14 and 25?
age = 17
print(14 <= age <= 25)    #hence its 'True'

age = 56
print(14 <= age <= 25)    #hence it will be "False"





'''------------LOGICAL OPERATORS------------'''

age = 25
has_license = True

#AND both must be true
can_drive = age >= 16 and has_license
print(can_drive)  #True
age = 25
can_drive = age >= 16 and not has_license
print(can_drive)

#OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend) #True

# NOT - reverses the value
age = 45
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False

age = 17
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # True



'''----------------Truth tables-----------------'''

# AND: Both must be True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# OR: At least one must be True  
print(True or False)    # True
print(False or False)   # False

# NOT: Flips the value
print(not True)         # False
print(not False)        # True



'''------------Assignment shortcuts-------------'''

score = 9

# Instead of:

score = score + 10

# Write:
score += 10
print(score)

# Works with all operators
x = 10
x += 5    # x is now 15
x *= 2    # x is now 30


'''------------String manipulation--------------'''



#JOINING

first_name = "Eman"
last_name = "Touqeer"
full_name = first_name + " " + last_name
print(full_name)

name = "Ahmad"
new_way_to_print = f"Hi there, my name is {name}!"
print(new_way_to_print)

#Reepetetion

star = "*"
stars = star * 10  # "**********"

separator = "-" * 20  # "--------------------"



#changing cases

text = "Peaky Blinders"

print(text.lower())    # "peaky blinders"
print(text.upper())    # "PEAKY BLINDERS"
print(text.title())    # "Peaky Blinders"


# Finding and replacing

# check if something exists
movie = "Game of Thrones"         
print("Thrones" in movie)
print(movie.startswith("Game"))
print(movie.endswith("Thrones"))   
# find position
print(movie.find("Game"))   # 1st occurance "0"
print(movie.count("of"))    # no. of times "1"

#replace
new_movie = movie.replace("Game of Thrones", "Whiplash")
print(new_movie)      # "Whiplash"









