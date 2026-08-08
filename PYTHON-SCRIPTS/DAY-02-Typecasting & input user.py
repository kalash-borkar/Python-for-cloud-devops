# Type casting and input user

a=1
print(type(a))

b='1'
print(type(b))

c=int(b) #type cast b as string into integer
print(type(c))
print(a+int(b))
print(a+c)


a = 4.5
print(type(a))

# Implicit type casting

var1=10
var2=23.8
var3=var1+var2
print(var3)
print(type(var3))


#Input functions

a=input()
print(a+a) # Input functions always read value as string
print(int(a)+int(a)) #we have change data type of a thriugh typecasting now automatically it will perform arithmatic operations

name = input("Enter your name: ")
Age = input("Enter your age: ")
print(f"Hello,{name} what is your{Age}")

age=input("Enter your age: ")
print(f"Ohh,you are just {age}")
print(f"Next year you will be {int(age)+1}") #since we need +1 in age ,we need to typecast asge and change age data type into int cause Input functions always read value as string

# #Input from user to add 2 numbers and print results.

x=input("Enter first number: ")
y=input("Enter second number: ")
print(f"Sum of {x}and{y} is {int(x)+int(y)}")

#practice for input and typecasting


# Write a program to input student name & marks of 3 subjects. Print name & percentage in output. 

student_name = input("Enter Your name: ")
hindi_marks = input("Enter Your Hindi_marks: ")
maths_marks = input("Enter Your maths_marks: ")
science_marks = input("Enter Your science_marks: ")
physics_marks = input("Enter your physics_marks: ")

# Percentage calculate
percentage = ((int(hindi_marks) + int(maths_marks) + int(science_marks) + int(physics_marks))/400)*100

print(f"The result of {student_name} is {int(percentage)}%. well done!")


# Q2: Write a program that collects multiple types of data to store in a dictionary  and print output.

#initialize dictionary

User_data = {}

#input from user

User_data['name'] = input("Enter your name: ")
User_data['age'] = int(input("Enter your age: "))
User_data['height'] = float(input("Enter your height: "))
User_data['Student'] = input("Are you student (yes/no)")

print(User_data)