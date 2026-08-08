print ('Hello kalash')

# Variables and constaints,data types basic:

name = "kalash"
age = 25
salary = 50000

print (f"My name is {name} & i am {age} years old, i am earning approx. {salary} per month")


a = 5
print(a)

#This is variable
learner = 'kalash borkar' #words,sentence use quotes
# print('Python by',learner)
print('python by',learner, sep='-')


#Calcualtions in python
a=10
b=11
c=34
print(a+b+c)
print(a-b-c)
print(a*b*c)
print(a+b/c)


kalash=15
d=kalash
print(d)

#assign variable in one
a,b,c = 11,22,33
print(a,b,c)
print(a+b+c)

#ways to delare variable

Myname = 'kalash' #pascal case
myName = 'kalash' #camel case
myname = 'kalash' #flat case
my_name = 'kalash' #snake case


#Data types in python

a='1'
b='2'
print(a+b)  #we cannot perform arithmatic operation string it combines the variables and gives the output
print(type(a),type(b)) #checking the data type: str


a = [1,2,4,4,5] #list data type
print(type(a))

a = (1,2,4,4,5) #tupe data type
print(type(a))

my_dict = {'name':'kalash','age':25,'city':'nagpur'} #dictionary data type assign shopuld be in curly bracket
print(type(my_dict))

my_sets={1,2,2,3,4,'kalash'} #set data type
print(type(my_sets))

bool1=True
bool2=False
print(type(bool1),type(bool2))


#Assignment no.1

# Q1: Write a Python program that prints the following text exactly as it appears: 
print('python is fun.')
print('''"Quotes" and 'single quotes' can be tricky''')

print("python is fun.\n\"Quotes\" and 'single quotes' can be tricky.")



# Q2: For a business create 3 variables to store- name, age, and city. 
# Then print a sentence that uses these variables.

Name = 'Kalash Borkar'
age = 25
city = 'Nagpur,Maharashtra'
print("Hello,my name is",Name, "i am" ,age, "years old & i am from",city)


#Using Formatted string
print(f"My name is {Name},i am {age} years old,and i am from {city}")