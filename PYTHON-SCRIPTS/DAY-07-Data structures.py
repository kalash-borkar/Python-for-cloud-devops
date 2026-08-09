#data structures in python ''
#lists in python

my_list = [1,2,3,4,5,'kalash','borkar'] #mixed data type
print(my_list)
print(type(my_list))

kalash = [1,2,['kalash','borkar'],3,3,4,8]  #nested list
print(kalash)
print(type(kalash))

#accessing list through indexing

kalash = [1,2,3,4,5,6,7,8,8]
kalash[3]
print(kalash[3])

#to check elements using negative index
kalash[-1]
print(kalash[-1])  #accessing last element
print(kalash[-2])

#Slicing in list
kalash = [11,22,33,44,55,66,77,88,99,111,222,333]
print(kalash)
print(kalash[1:6])
print(kalash[0:6])
print(kalash[2:5])
print(kalash[-3:])

print(kalash[::2]) #alternate elements
print(kalash[::-1]) #reverse list


#Tuple data structure

kalash = (1,2,3,34,54,5)
kalash1 = tuple((1,2,3,34,54,5))
print(kalash1)
print(type(kalash1))

#coverting a list into tuple
kalash = [11,22,33,44,55,66,77,88,99,111,222,333]
kalash2 = tuple(kalash)
print(kalash2)
print(type(kalash2))

# Dictionary in Python

#syntax: 
# my_dict = {'key1':'value1', 'key2':'value2', ...}

#Methods to create dictionary 
# method-1 create dictionary using curly braces 
cohort = {'course':'Python', 
          'Instructor':'Rishabh Mishra', 
          'Level': 'Benginner'} 

print(cohort)
print(type(cohort)) 

# Method-2 using dict() constructor 
person = dict(name= 'Madhav', age=20, grade = 'A')
print(person)
print(type(person)) 

# Method-3 using list of tuples 
person2 = dict([('name', 'Madhav'), ('age', 20), ('city', 'Mathura')])
print(person2)
print(type(person2)) 

# Access dictionary values 
student = {
    1: 'Class-X',
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

print(student)
print(type(student)) 

print(student['name'])
print(student['grade'])


# Dictionary Methods 
student = {
    1: 'Class-X',
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

# keys
print(student.keys())

# values
print(student.values())

# items
print(student.items())

# get
print(student['name'])
print(student.get('email', 'Nahi hai')) 


# Add/modify items in dictionary 
student = {
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

# add item - assign operator
student['email'] = 'madhav@example.com'
print(student)

# modify/replace item - assign operator
student['grade'] = 'A+'
print(student) 

# remove items
# del to remove item 
del student['grade']
print(student)

# pop method
var1 = student.pop('email')
print(var1)
print(student)


# dictionary iteration 
student = {
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

# loop through keys 
for keys in student:
    print(keys)

# loop through values
for value in student:
    print(student[value]) 

# using .values() method
for value in student.values():
    print(value)

# loop through both key-value pair  
for keys,value in student.items():
    print(keys, value) 


# Nested dictionary 

main_student = {

    'student1' : {'name': 'Madhav', 'age': 20},
    'student2' : {'name': 'Keshav', 'age': 25, 'grade': 'A'}
} 

print(main_student)

# access value 
print(main_student['student1'])

print(main_student['student1']['name'])
print(main_student['student2']['grade'])


# Dictionary comprehension 

# syntax 
# new_dict = 
# {key_exp : value_exp for item in iterable if condition}

my_dict = {x:x+x for x in range(1,6)}

print(my_dict) 

# Sets in Python 

# charaterstics of set 
#1. unique values/items 
#2. unordered - no indexing 
#3. mutable- add/remove elements
#4. Immuatable elements - replace/modify existing elements 

# create set using curly braces 
my_set = {1,2,3}
print(my_set)
print(type(my_set))

# create set using set constructor 
my_set2 = set([4,5,6]) 
print(my_set2)  

# set operations
#adding elements
numbers = {1,2,3,4} 
numbers.add(100)
print(numbers) 

# removing elements 
#remove 
fruits = {'apple', 'mango', 'banana'}
# fruits.remove('banana') # if element not present show error
print(fruits) 

#discard 
fruits.discard('apple') # doesn't show error
print(fruits)


# Set Methods
#1. union - combine elements from 2 sets 
set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
# print(union_set) 

# union alternative 
union_set2 = set1 | set2 
# print(union_set2) 

#2. Intersection - common elements 
set1 = {1,2,3,4}
set2 = {3,4,5}
inter_set = set1.intersection(set2)
# print(inter_set) 

# intersection alternative 
inter_set2 = set1 & set2 
# print(inter_set2) 

#3. Difference - element present in first set only but not in second set 
set1 = {1,2,3,4}
set2 = {3,4,5}
diff_set = set1.difference(set2)
# print(diff_set) 

# Difference alternative 
diff_set2 = set1 - set2 
# print(diff_set2) 

#4. Symmertic Difference - element in either set but not in both 
set1 = {1,2,3,4}
set2 = {3,4,5,6}
sdiff_set = set1.symmetric_difference(set2)
# print(sdiff_set)

# Symm Diff alternative 
sdiff_set2 = set1 ^ set2 
# print(sdiff_set2)


# Set Iterations
# for loop
numbers = {1,2,3,4,5}
for i in numbers:
    print(i)

# while loop - doesn't support 


# Set compreshesion 
squares = {x**3 for x in range(1,6)} 
print(squares)



# Assignment-6 
# on List, Tuple, Set & Dict 
# data structures / collection dtype

# Q1 Find the Intersection (common elements) of Two Lists? 

list1 = [1,2,4,5]
list2 = [4,5,6,7,8]

# using for loop 
def intersection_loop(lst1, lst2):
    common_list = []
    for item in lst1:
        if item in lst2 and item not in common_list:
            common_list.append(item)
    return common_list 

# print(intersection_loop(list1, list2)) 

# using List comprehension 
def intersection_comp(lst1, lst2):
    return [item for item in lst1 if item in lst2] 

# print(intersection_comp(list1, list2)) 


# Q2 Find the Most Frequent Element in a List? 
numbers = [1,2,2,3,3,3,4,7,7,7,7]

def most_freq(lst):
    max_count = 0 
    most_freq = None 
    for item in lst:
        count = lst.count(item)
        if count > max_count:
            max_count = count 
            most_freq = item 
    return most_freq 

# print(most_freq(numbers))


# Q3 Find Cumulative Sum of a List
numbers = [1, 2, 3, 4]

def cumulative_sum(lst):
    cum_sum = [] 
    total = 0 
    for num in lst: 
        total += num 
        cum_sum.append(total) 
    return cum_sum 

# print(cumulative_sum(numbers)) # Using List Comp: print([sum(numbers[:i + 1]) for i in range(len(numbers))])


# Q4 Remove Duplicates from a List 
fruits = ["apple", "banana", "mango", "apple", "banana"]

# using loop 
def remove_duplicates(lst):
    unique = []
    seen = set()
    for item in lst: 
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique 

# print(remove_duplicates(fruits)) 

# without seen, but not good for large dataset -list
def remove_duplicates(lst):
    unique = []
    for item in lst: 
        if item not in unique:
            unique.append(item)
    return unique 

# print(remove_duplicates(fruits))  

# using set constructor 
# print(list(set(fruits))) 


# Q5 Find the index of an element in a tuple
my_tuple = (1, 10, 2, 3, 4)

def find_index(tup, elem):
    return tup.index(elem) if elem in tup else -1

# print(find_index(my_tuple,100))


# Q6 Find the Most Frequent Value in a dictionary
data = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1} 

def most_freq(dct):
    frequency = {}
    for value in dct.values():
        if value not in frequency:
            frequency[value] = 0
        frequency[value] += 1 # 1:1, 2:1, 1:2,3:1, 1:3
    max_value = max(frequency, key=frequency.get)
    return max_value

# print(most_freq(data)) 


# Q7 Merge Dictionaries with Summation 

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 35, 'd': 25} 

def merge_dict(dict1, dict2):
    result = dict1.copy() 
    for key, value in dict2.items():
        if key in result:
            result[key] += value 
        else:
            result[key] = value 
    return result 

# print(merge_dict(dict1, dict2)) 
 

# Q8 Flatten a Nested Dictionary 

data = {'a': {'b': {'c': 42}, 'd': 7}, 'e': 10}
#o/p {a.b.c: 42, a.d: 7, e: 10}

# a, e 
# {'b': {'c': 42}, 'd': 7}
# b, d
# {'c': 42}

def flatten_dict(data, parent_key= '', sep = '.'):
    items = {} #initialize empty dict to store flattened items
    for key, value in data.items(): 
        # combine current key with parent key
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict): # check if dict or not
            # recursive flatten the nested dict
            items.update(flatten_dict(value, new_key, sep))
        else:
            # adding key-value to flatten dict
            items[new_key] = value 
    return items 

# print(flatten_dict(data)) 

# data = [1,2,4]
# print(isinstance(data, list)) 


# Q9 Sort a Dictionary by Values

data = {'a': 5, 'b': 9, 'c': 2, 'd': 7} 

# [('a',5), ('b', 9)....]

def sort_by_values(data):
    sorted_items = sorted(data.items(), 
                          key = lambda item: item[1],
                          reverse=True)
    return {key: value for key , value in sorted_items} 

print(sort_by_values(data)) 

# print(sorted([1,2,0,2,8], reverse=True))

# print(data.items())


# Q10 Access values from a nested dictionary 

data = {
    "level1": {
        "level2": {
            "level3": {
                "value1": 10,
                "value2": [1, 2, {"deep_key": 42}],
                "value3": {"inner_key": "target"}
            },
            "other_key": 99
        },
        "list_key": [
            {"list_inner_key1": 88},
            {"list_inner_key2": {"deep_list_key": 77}}
        ]
    }
}

#  Tasks to Access Elements:
# Retrieve 42 
# Retrieve "target" 
# Retrieve 77


# 10 Access values from a nested dictionary – Solution

# Tasks to Access Elements
# Retrieve 42. Path: data -> level1 -> level2 -> level3 -> value2 -> [2] -> deep_key
print(data["level1"]["level2"]["level3"]["value2"][2]["deep_key"])

# Retrieve "target". Path: data -> level1 -> level2 -> level3 -> value3 -> inner_key
print(data["level1"]["level2"]["level3"]["value3"]["inner_key"])

# Retrieve 77. Path: data -> level1 -> list_key -> [1] -> list_inner_key2 -> deep_list_key
print(data["level1"]["list_key"][1]["list_inner_key2"]["deep_list_key"])