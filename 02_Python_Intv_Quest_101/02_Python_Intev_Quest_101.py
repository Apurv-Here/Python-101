# 01 Python Interv Quest 101


# -------------------------------------------------------------

# 1. Reverse a string in python

s1 = "abc"

s2 = ""

s1_len = len(s1)

lst1 = [34, 45, 67]
lst1.sort()
lst1.sort(reverse = True)
# This sort function works only on list and not strings




print("Normal traverse")

for i in range(0, s1_len):
    print(s1[i], end = ' ')

print()
print("\nReverse traverse")

for i in range(s1_len - 1, -1, -1):
    print(s1[i], end = ' ')
    

# Appending reverse for loop in blank string

for i in range(s1_len-1, -1, -1):
    s2 += s1[i]
    
print("\nReverse string is : ")
print(s2)


"""
o/p:

Normal traverse
a b c 

Reverse traverse
c b a 
Reverse string is : 
cba

"""


# -----------------------------------------------------------

# sorted function is used to sort strings
str1 = "zaabc"
str2 = "aazbc"

temp1 = sorted(str1)
# temp 1 is now a list ['a', 'a', 'b', 'c', 'z']

temp2 = sorted(str2)

print(temp1)
print(temp2)
print(type(temp1))


"""
o/p:

['a', 'a', 'b', 'c', 'z']
['a', 'a', 'b', 'c', 'z']
<class 'list'>

"""


# -----------------------------------------------------------

# Counter method for string

from collections import Counter 

str1 = "abbbccsd"

temp1 = Counter(str1)

print(temp1)
print(type(temp1))


"""
o/p:

Counter({'b': 3, 'c': 2, 'a': 1, 's': 1, 'd': 1})
<class 'collections.Counter'>

"""


# -----------------------------------------------------------

# Find the items greater than itself after its index in a python list
# Public Sapient

input = [99, 28, 12, 55, 13, 15, 76, 99]

inp_len = len(input)

# for i in input:
#     count = 0
#     output_list = []
#     ele = input(i)
#     for j in range(input.index())

for i in range(0, inp_len, 1):
    temp = input[i]
    counter = 0
    out_list = []
    
    for j in range(i+1, inp_len, 1):
        if(input[j] > temp):
            counter =+ 1
            out_list.append(input[j])
        
    print(temp, counter, out_list)



"""
o/p:

99 0 []
28 1 [55, 76, 99]
12 1 [55, 13, 15, 76, 99]
55 1 [76, 99]
13 1 [15, 76, 99]
15 1 [76, 99]
76 1 [99]
99 0 []

"""


# -----------------------------------------------------------

#Flatten the list
# input = [1, 2, [7, 9, [15, [12, 9,]], 18, 10]]
# output = [1, 2, 7, 9, 15, 12, 9, 18, 10]
# Delloite



def f_flatten(input_list):
    l = []
    
    for i in input_list:
        if(type(i) is list):
            # Imp step
            
            l.extend(f_flatten(i))
            
        else:
            l.append(i)
    
    return l

if __name__ == "__main__":
    
    input = [1, 2, [7, 9, [15, [12, 9,]], 18, 10]]
    
    print(f_flatten(input))


"""
o/p:

[1, 2, 7, 9, 15, 12, 9, 18, 10]

"""


# -----------------------------------------------------------

# PWC
# Find Student name with Maximum Marks from List of Tuple

students = [('David', 46), ('Sam', 56), ('Sagar', 90)]

for i in students:
    name = i[0]
    marks = i[1]
    print(name, marks)
    
def get_highest_score(input_list:list)->list:
    if len(input_list) == 0:
        return []
    
    max_marks = max(marks for name, marks in input_list)
    
    res_list = [(name, marks) for name, marks in input_list if marks == max_marks]
                
    return res_list
                

# Answer in list
print(get_highest_score(students))

# Answer not in list, in this case it will be tuple
print(*get_highest_score(students))


"""
o/p:

David 46
Sam 56
Sagar 90
[('Sagar', 90)]
('Sagar', 90)

"""


# -----------------------------------------------------------

# Accenture
# Count of each alpha in strings
# input s='bbbbcccaad'
# output = [4,3,2,1]

s='bbbbcccaad'

# Using Counter
from collections import Counter


# Using Dictionary:

freq={}
for key in s:
    if key in freq.keys():
        freq[key]+=1
    else:
        freq[key]=1
        
print(list(freq.values()))


"""
o/p:

[3, 4, 1, 2]
[4, 3, 2, 1]

"""


# -----------------------------------------------------------

# TCS
# Common letters in two strings

"""
Find out common letters between two strings
Find out all letters between two strings
Find out letters which is present in one string but not present in second, vice versa
"""

input1 = "sagar prajapati"
input2 = "geekcoders"

def common_alpha(input1:str, input2:str)->list:
    input1_set = set(input1)
    input2_set = set(input2)
    
    print(input1_set, input2_set)
    
    print("Printing common Letters: ")
    print(input1_set & input2_set)
    
    print("Printing all Letters: ")
    print(input1_set | input2_set)
    
    print("Printing letters which is present in one string but not present in second: ")
    print(input1_set - input2_set)

    

common_alpha(input1, input2)



"""
o/p:

{'j', 'p', 'i', 'g', 's', 't', 'r', ' ', 'a'} {'k', 'c', 'e', 'g', 's', 'o', 'r', 'd'}
Printing common Letters: 
{'r', 'g', 's'}
Printing all Letters: 
{'k', 'j', 'p', 'i', 'c', 'e', 'g', 's', 't', 'r', 'o', ' ', 'd', 'a'}
Printing letters which is present in one string but not present in second: 
{'j', 'p', 'i', 't', ' ', 'a'}

"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------




"""
o/p:



"""


# -----------------------------------------------------------


