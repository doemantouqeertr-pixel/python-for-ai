

"""-------------CONTROL FLOW---------------

> Control flow:

Make your programs smart with decisions
​
> Making programs think:

So far, your programs run top to bottom, 
executing every line. But real programs need
to make decisions - 
“if this, then that”.

"""















#  ------------ IF STATEMENTS ---------------



# If, else, elif :

temperature = 25
if temperature > 25:
    print("It's Hot")
else:
    print("It's a nice weather!")




temperature2 = 15
if temperature2 > 25:
    print("It's Hot")
elif temperature2 < 18:
    print("OMG it's too Cold")
else:
    print("It's a nice weather")




score = 67

if score >= 90:
    print("A - Excellent")
elif score >= 80:
    print("B - Good Job!")
elif score >= 70:
    print("C - keep it up!")
else:
    print("F - It's okay, you can do it")



# Multiple conditions

age = 17
has_license = True
if age >= 18 and has_license:
    print("You can drive!") #both must be true 
else:
    print("stay away, u can't drive")




has_ticket = True
age = 14
if has_ticket and age >= 18:
    print("Enjoy the movie bud!")
else:
    print("do 67 kid!")

has_ticket = True
age = 13
if has_ticket:   #we can also write liek this
    if age >= 18:
        print("enjoy the movie bud!")
    else:
        print("do 6-7 kid!")
else:
    print("Please buy a ticket man!")




day = "Monday"
weekend = (day == "Saturday" or day == "Sunday")
holiday = (day == "Friday")

if weekend or holiday:
    print("No work day!")
else:
    print("It's a working day!")





weather = "sunny"
raining = not (weather == "sunny")
if not raining:
    print("lets playyyy")

weather = "sunny"
if weather == "sunny":
    print("lets playyyy")
else:
    print("stay inside")






















#  ----------------- LOOPS --------------------


'''
loops let you repeat code without writing it multiple times, 
instead of copying and parting, you tell python  to repeat 
for you.

> without loops:
  print("Hello World!")
  print("Hello World!")
  print("Hello World!")
  print("Hello World!")
  print("Hello World!")

> with loops:
  for i in range(5):
    print("Hello World!")

'''














# for loops

for i in range(3):
    print(i) # output: 0 (bcz pythong starts counting from 0)
                     # 1
                     # 2
                
for i in range(4):
    print("Ovarian Lottery") # it will print it 4 times


# counting from different starting points

for i in range(0, 5):
    print(i) # output will be: 0
                            #  1
                            #  2
                            #  3
                            #  4

for i in range(0,10,2):
    print(i) #means we wanna go from 0 to 10 but we wanna do in steps of 10
    # out out will be 0,2,4,6,8










