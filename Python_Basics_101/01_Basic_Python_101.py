

# ---------------------------------------------------------

# length function

s1 = "abc"

s2 = ['d', 'e', 'f', 'g']

n1 = len(s1)

n2 = len(s2)

print("Lenght of s1 is :", n1)
print("Lenght of s2 is :", n2)


"""
o/p:

Lenght of s1 is : 3
Lenght of s2 is : 4

"""


# ---------------------------------------------------------

# for loop basic
# for loop printing on same line

s1 = "abcdef"
n1 = len(s1)

for i in range(0, n1):
    print(s1[i])
    
print()

for i in range(0, n1):
    print(s1[i], end = " ")
    
print()


"""
o/p:

a
b
c
d
e
f

a b c d e f 

"""


# ---------------------------------------------------------

# list traversal with for loop 
# with increment as well

list1 = [1, 3, 5, 6, 9]
n1 = len(list1)

print("Forward traversal of list")

for i in range(0, n1):
    print(list1[i], end = " ")
    
    
print()
print()
print("Forward traversal of list with two increment")

for i in range(0, n1, 2):
    print(list1[i], end = " ")


"""
o/p:

Forward traversal of list
1 3 5 6 9 

Forward traversal of list with two increment
1 5 9

"""


# ---------------------------------------------------------

# Reversal traversal of list with for loop
# Reversal traversal with two increment

list1 = [1, 3, 5, 6, 9]
n1 = len(list1)

print("Reverse traversal of list")

for i in range(n1 - 1, -1, -1):
    print(list1[i], end = " ")
    

print()
print()
print("Reverse traversal of list with two increment")

for i in range(n1 - 1, -1, -2):
    print(list1[i], end = " ")


"""
o/p:

Reverse traversal of list
9 6 5 3 1 

Reverse traversal of list with two increment
9 5 1

"""


# ---------------------------------------------------------

# if else 

a = 3

if (7 - 4) == a:
    print("True")
else:
    print("False")


"""
o/p:

True

"""

# ---------------------------------------------------------

# set operations (creating and finding elements in set)

set1 = set();

set1 = {1,1,1,2,3,2,1,4,6,8,1};
print("Normal set with integers:")
print(set1)


# creating an empty set
set2 = set()
print()
print("printing an empty set:")
print(set2)

# creating set with string
set3 = set("GeeksForGeeks")
print()
print("Printing set with characters:")
print(set3)

# Creating a Set with the use of a List
print()
print("Creation of set with list")
set4 = set(["Geeks", "For", "Geeks"])
print(set4)


# Creating a Set with the use of a dictionary
set5 = {"Geeks": 1, "for": 2, "Geeks": 3}
print()
print("Printing set with dictionary:")
print(set(set5))


# searching for exact element in set
print()
print("Searching for elements in set:")
if 1 in set1:
    print("1 is there");
else:
    print("no, search different element")
    


"""
o/p:

Normal set with integers:
{1, 2, 3, 4, 6, 8}

printing an empty set:
set()

Printing set with characters:
{'G', 'o', 'e', 'r', 's', 'k', 'F'}

Creation of set with list
{'Geeks', 'For'}

Printing set with dictionary:
{'Geeks', 'for'}

Searching for elements in set:
1 is there

"""

# ---------------------------------------------------------

# adding and removing elements in set
# add()
# pop() -- removes the last element

# adding by add and uodate method

set1 = set()
set1.add(2)
set1.add(3)
set1.add(5)
set1.add(5)
print(set1)

print()

# Update method is given list 
# With this we can add multiple elements at once
set1.update([9,7,5,6,6,6])
print(set1)



# Removing elements in set
# pop method: It removes at random
print()
print("Removing elements in set:")
print("Set before pop method:")
print(set1)
# set1.pop()
print("Set after pop method:")
print(set1)


# Removing specific item from set
print()
print(set1)
print("Removing 3 from set:")

set1.remove(3)
# Be careful when you use remove method
# It will throw an error if item is not present in set
# set1.remove(1)

print(set1)


# Discard method: does same as remove but it doesn't give error when element is not present in set
set1.discard(999)
set1.discard(9)
print()
print("Removing specific element using discard method")
print(set1)


# Clearing the whole set
# set1.clear()


"""
o/p:

{2, 3, 5}

{2, 3, 5, 6, 7, 9}

Removing elements in set:
Set before pop method:
{2, 3, 5, 6, 7, 9}
Set after pop method:
{2, 3, 5, 6, 7, 9}

{2, 3, 5, 6, 7, 9}
Removing 3 from set:
{2, 5, 6, 7, 9}

Removing specific element using discard method
{2, 5, 6, 7}

"""

# ---------------------------------------------------------

# Operations on set
# Union, Intersection, Difference & Symmetric Difference


"""
o/p:



"""

# ---------------------------------------------------------



# ---------------------------------------------------------




"""
o/p:



"""

# ---------------------------------------------------------



# ---------------------------------------------------------




"""
o/p:



"""

# ---------------------------------------------------------



# ---------------------------------------------------------




"""
o/p:



"""

# ---------------------------------------------------------



# ---------------------------------------------------------




"""
o/p:



"""

# ---------------------------------------------------------



# ---------------------------------------------------------




"""
o/p:



"""

# ---------------------------------------------------------


