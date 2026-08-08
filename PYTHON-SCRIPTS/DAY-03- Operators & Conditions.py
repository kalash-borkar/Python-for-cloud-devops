# #Operators and Conditonals statements

a=100
b=39
print(a+b)
print(a-b)
print(a*b)
print(a/b)   #arithmatic operators
print(a<b)


a=100
b=39
print(a>100 and b<100)
print(a==100 and b==100) #Equals operators

# #Conditionals statements
# #if statement works for only true conditions

age = 35
if age > 30:
    print("yes you are right,he is 35") #if statement


a=14
b=15
if a<b:
    print("a is greater than b")

age = int(input("Enter your age")) #Inout for an user for age   
if age > 19:
    print("You are an adult")



# #if else statements

tempreture = 30
if tempreture > 20:
    print("It is hot day")
else:
    print("It is cold today")


# #if-elif-else statements

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("you comes under GRADE: A")
elif marks >= 80:
    print("you comes under GRADE: B")
elif marks >= 70:
    print("you comes under GRADE: C")
else:
    print("you comes under GARDE: D")
  
# #Nested if else statements:

number = int(input("enter your number: "))

if number > 0:
    if number % 2 ==0:
        print("This is even number")
    else:
        print("This is odd number")
else:
    if number == 0:
        print("This is zero")
    else:
        print("This is negative number")


# #Conditionals expressions

age = 16
status = "Major" if age >= 18 else "Minor"
print(status)

#assignment for conditional statements

# Q1: Leap Year: Write a simple program to  determine if a given year is a leap year using user input.

year = int(input("Enter a year (eg. 2024): "))

if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} this is not a leap year")

# Q2: Login Authentication using conditional statement. 
# Assume you have a predefined username and password. 
# Write a program that prompts the user to enter a username and password and checks whether they match. 
# Provide appropriate messages for the following cases:
# Both username and password are correct.
# Username is correct but password is incorrect.
# Username is incorrect.

predefined_username = 'kalash'
predifined_password = '1d234k'

username = input("Enter your username: ")
password = input("Enter your username: ")

if username == predefined_username:
    if password == predifined_password:
        print("Welcome, login was successfull")
    else:
        print("Password is incorrect")
else:
    print("username is incorrect.")

# Q3: Admission Eligibility: A university has the following 
# eligibility criteria for admission:
# Marks in Mathematics >= 65
# Marks in Physics >= 55
# Marks in Chemistry >= 50
# Total marks in all three subjects >= 180 OR- 
# -Total marks in Mathematics and Physics >= 140
# Write a program that takes marks in three subjects as input and prints whether the student is eligible for admission.

print("Enter PCM marks out of 100")
Mathematics_marks = int(input("Enter your mathematics marks: "))
Physics_marks = int(input("Enter your physics marks: "))
Chemistry_marks = int(input("Enter your chemistry marks: "))

if Mathematics_marks >= 65 and Physics_marks >= 55 and Chemistry_marks >=50 and \
   (Mathematics_marks + Physics_marks + Chemistry_marks) >=180 or (Mathematics_marks + Physics_marks) >= 140:
   print("You, are eligible enough")

else:
    print("You, are not eligible")

   
