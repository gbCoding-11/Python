
# Create variables

red_bucket = "kevin"
red_bucket = 10         # we don't need to input the type like strings, int...etc.
#print(red_bucket)       # Output = 10 // variables = last value
print(type(red_bucket))  # Output = int

del red_bucket           # delet variables
print (red_bucket)         # Output = NameError: name 'red_bucket' is not defined


# input fuction
blue_bucket = input("what do you want to input the blue bucekt?")
print(blue_bucket  )

#conditional logic -true or false /simple one
print( 5==4 )    #Output = false
print( 5!=4 )     # Output = true

Tomas_Age = 3
Age_at_Kindergarten = 5
print(Tomas_Age == Age_at_Kindergarten)     #Output = false


#multiple different criteria - If statement
Thomas_Age = 10
Age_at_Kindergarten = 5

if Thomas_Age < Age_at_Kindergarten:
    print("Thomas should be in the pre-scholl")
elif Thomas_Age == Age_at_Kindergarten:
    print("Enjoy kindergarten")
else:
    print("Thmoas should be in another class")


#fuction - subroutine
#print fuction
def print_kevin():              # define a function
    text = "kevin has a great channel"
    print(text)
    print(text)
    print(text)

print_kevin()    # call the function
print_kevin()
print_kevin()


# If statement within a function
def school_age_calculator(age,name):        #define a function
    if age < 5:
        print("Enjoy the time!", name,"is only",age)
    elif age == 5:
        print("Enjoy kindergarten",name)
    else:
        print("They grow up so fast!")

school_age_calculator(3,"Jenny")        #call the function



#return a value from a function
def add_ten_to_age(age):        #define a function
    new_age = age + 10
    return new_age

How_Old_Will_I_Be = add_ten_to_age(3)
print(How_Old_Will_I_Be)           #call the function



#Loop function - Loop 1. while
x=0
while(x<5):
    print(x)        # It'll keep executing until it reaches 4
    x=x+1


#Loop function - Loop 2. For
for x in range(5,10):
    print(x)                #but it doesn't include 10 : Output 5~9



#Another loop example  +break
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

for d in days:
    if(d=="Thu"):break      # stop    /Output : Mon,Tue,Wed
    print(d)


#Another loop example   +continue
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

for d in days:
    if(d=="Thu"):continue      # to skip "Thu" /Output : Mon,Tue,Wed,Fri,Sat,Sun
    print(d)


#Libraries and Modules  - ex)pi
import math
print("pi is", math.pi)     




