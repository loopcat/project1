import re


# variable types - variables are objects, you do not need to declare before using them or declare types
# integers and floating point number; complex numbers also supported
intNumber = 1
floatNumber = 1.0

# divide integers  a // b

# divide floating   a / b

# can asign multiple variables on the same line
intX, intY = 1, 2

#=================================================================================================
# STRINGS
#=================================================================================================
# strings can be single or double quotes (use double quotes to include an apostrophe in the string
# position starts with 0

# concatenate using + sign
strName = "Jenny"
strLastName = 'Weber'
newString = strName + strLastName

print(strName + " cat")

# to cat a string and a number use str to convert integer to string
print(strName + str(6))

# split and join (split gives a list of items)
testString = "This is a test"
testString = testString.split(" ")  # split on space: ["this", "is", "a", "test"]
testString = "-".join(testString)   # join with hyphen:  "this-is-a-test"

# string functions use .  You can use repeated functions with more .   strName.capitalize().isupper()
# it looks like capitalize will ignore a number (alphanumberic) - only capitalizes the 1st char of a string
strName = 'jenny lee'
print(strName.capitalize())  # Jenny lee

# use [] to access individual characters
print(strName[0])

# swap case function
stringTest = "Jenny"
print(stringTest.swapcase())

# find a substring.  **IF using the end index it must be 1 past the occurance.
# For Example:  First occurance of cat is index 0:  newString.find(sub,0,3)
#               second occurance of cat is index 11:  newString.find(sub,11,14)
#               third occurance of cat is index 19:  newString.find(sub,19,22) it is OK if end index is past the string
newString = "cat in the cat hat cat"
sub = "cat"
print(newString.find(sub,19,22))

# findall - need to import re (findall does not work with overlapping, use look ahead)
text = 'catchatcatch'
pattern = 'at'
print(re.findall(pattern,text))    # ['at', 'at', 'at']
repeats = len(re.findall(pattern,text))
print(repeats)    # 3

# using look ahead to find overlapping substring
#text = 'BANANA'
#subtext = 'ANA'
#print(re.findall(r'(?=(ANA))',text))
#print(re.findall(r'(?=('+ subtext +'))',text))

# text wrap - break a string apart
newString = 'abcdefghijklmnopqrstuvwxyz'
#newString = textwrap(newString,4)  # gives you ['abcd', 'efgh',....]  use join to put back together

# string formats for printing numbers in decimal, hex, binary, octal etc.
# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.4567898))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))

# boolean - True and False must start with capital letter
boolDone = True

# ***************         *********************     *****************
# linefeed is automatic.  If you add a linefeed you will get 2 lines

# print without linefeed
print("Hello", end="")   # no line feed
print()  # makes 1 linefeed


#=================================================================================================
# type conversions
#=================================================================================================

# int()   converts string, floating point to integer
# float() converts string, integer to float
# str()   converts integer, float, list, tuple, dictionary to string
# list()  converts string, tuple, dictionary to list
# tuple() converts string, list to tuple

number = 16

# convert integer to string
string1 = str(number)
print("string: ", string1)

# convert string to list
list1 = list(string1)
print("list1: ", list1)

# make copy and reverse
list2 = list1.copy()
list2.reverse()
print("list2: ", list2)

# compare if two lists are the same
if list1 == list2:
    print("True")
else:
    print("False")

#=================================================================================================
# STANDARD INPUT
#=================================================================================================

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "you are " + age + " years old")

# read two numbers seperated by a space in to two variables
# 1 3
n, m = [int(x) for x in input().split()]    # n=1 and m=3

# read a list of numbers separated by a space in to a list
# 1 3 5
list1 = [int(x) for x in input().split()]    # list1 = [1,3,5]

# same as above but create a set
seta = {int(x) for x in input().split()}     # seta = {1,3,5}

#=================================================================================================
# LISTS
#=================================================================================================

# lists - (a container to hold one or multiple types of items.  items are objects)
# index starts at 0   negatives start from the back of the list -1 is the last item

myList = ["apple", "toast", "butter"]
numberList = [1,2,3,4,5]

# print all the elements list
print(myList)
print(myList[0])  # prints "apple"
print(myList[1:])  # prints "toast", "butter"
print(numberList[2:4]) # prints 3,4 the 4th one is not included

#types can be mixed
myList = [1, "apple", True]

# list functions (extend, append, insert, remove, pop, index, count, sort, reverse, copy
oddNums = [1,3,5,7,9]
evenNums = [2,4,6,8]
oddNums.extend(evenNums)
print(oddNums)  # will print 1,3,5,7,9,2,4,6,8

oddNums.append(11)  # 1,3,5,7,9,11
oddNums.append([100,101])   # append a list inside of a list
evenNums.insert(2,10)  # 2,4,10,6,8
evenNums.remove(10)   # 2,4,6,8   (item to remove not the index
evenNums.clear()   # removes all, list is empty
oddNums.pop()  # removes last element

# search for an element
print(oddNums.index(5))   # will print the index for 5, if the item is not in the list, it errors out

# how many times an values exists in the list
oddNums = [1,3,5,5,7,9]
print(oddNums.count(5))   # returns 2 times

# sort the list
names = ["Mary", "Angie", "Tom", "Bob"]
names.sort()

# reverse the list
oddNums.reverse()

# copy to a new list
oddNums2 = oddNums.copy()     # oddNums2 is now a copy of oddNums

# comprehensive lists
# sample to print x,y,z coordinates up to a cube size 2 and only print coordinates that don't add up to n
x=2
y=2
z=2
n=2

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])

#=================================================================================================
# 2D lists  (lists of lists)
#=================================================================================================

# 4 rows 3 columns
numberGrid = [
    [1,2,3]
    [4,5,6]
    [7,8,9]
    [0]
]
# access by [row][col]
print(numberGrid[0][0])

#=================================================================================================
# SETS - do not allow duplicate items.  sets can contain mixed types
#=================================================================================================

a = set()   # must use () to create an empty set
a.add(1)
a.add(2)
a.add(2)# nothing will happen no duplicates added
print(a)  # prints {2, 1}

for x in a:
    print(x)
# create a set reading from input (integers separated by a space on a single line 1 3 4
seta = {int(x) for x in input().split()}     # seta = {1,3,4}

# update - adds items to set
a.update([1, 2, 3, 4]) # update() only works for iterable objects

# delete an item - remove will raise an error if item does not exist, pop - will raise an error if set empty
a.discard(10)
a.remove(1)
a.pop()

# union, difference and intersectection
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
a.union(b) # Values which exist in a or b
a.intersection(b) # Values which exist in a and b
a.difference(b) # Values which exist in a but not in b
a.union(b) == b.union(a)    # returns True
a.intersection(b) == b.intersection(a)     # returns True
a.difference(b) == b.difference(a)   # returns False

# use a set to remove duplicates from a list
list1 = [1,1,2,3,4]
new_set = set()
for x in list1:
    new_set.add(x)

# comparing subsets
#{1, 2} < {1, 2, 3}  # True
#{1, 2} < {1, 3}  # False
#{1, 2} < {1, 2}  # False -- not a *strict* subset
#{1, 2} <= {1, 2}  # True -- is a subset

# when adding to a list the order is not preserved, append does preserve the order

#=================================================================================================
# TUPLES
#=================================================================================================
# tuples -  constant (immutable)  format name = (x,y, ...) indexe start at 0

coordinates = (4,5)
print(coordinates[0])   # prints 4

multCoordinates = [(4,5), (2,3), (5,6)]    # list of tuples still immutable

# reading in integers seperated by a space to a tuple
numbers = tuple(map(int, input().split(" ")))
print(hash(numbers))

#=================================================================================================
# DICTIONARIES
#=================================================================================================
# dictionaries - allows information to be stored in key-value pairs.  retrieve values by key
#  name = {key: value, key: value, ...}
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
}

print(monthConversions["May"])
print(monthConversions.get("Feb"))
# default is key does not exist
print(monthConversions.get("Dec", "Not a valid key" ))

grades = {'Jane': [10, 7, 9], 'Bob': [2, 5, 7]}
print(grades.keys())
print(grades.values())
print(grades.items())
if 'Jane' in grades:
    print('Found')
    score = grades.get('Jane')
    print(score) # shows all the scores [10, 7, 9]
    score = grades.get('Jane', [])   # ssame thing

    print(score)
    ave = (score[0] + score[1] + score[2])/3
    print('%.2f' % ave)
else:
    print('Not Found')

#=================================================================================================
# FUNCTIONS
#=================================================================================================

# functions - ':' starts the function and code MUST be indented.

def printHi (person) :
    print("Hi" + person)

printHi("Jenny")

def cube(num) :
    return num ^ 3

print(cube(3))
result = cube(3)

#=================================================================================================
# MATH FUNCTIONS
#=================================================================================================

#=================================================================================================
# IF ELSE
#=================================================================================================
# if else - colon must follow condition with no spaces

x = 1
y = 10

if x > y and x > 1:
    print(x)
elif x == 0:
    print("x is 0")
elif y == 0:
    print("y is 0")
else:
    print(y)

#=================================================================================================
# WHILE LOOP
#=================================================================================================

i = 10
while i < 10:
    print(i)
    i += 1

#=================================================================================================
# FOR LOOP
#=================================================================================================

# will print 0 to 9
for i in range(10):
    print(i)

# with no line feed
for i in range(10):
    print(i, end = "") # 0123456789
    print(i, end =" ") # 0 1 2 3 4 5 6 7 8 9

# will print 3 to 9
for i in range(3, 10):
    print(i)

for letter in "a,b,c":
    print(letter)

friends = ["Ann", "Tom", "John"]
for name in friends:
    print(name)

for index in range(len(friends)):
    print(friends[index])

# nested for loop

for row in numberGrid:
    for col in row:
        print(col)

#=================================================================================================
# TRY / EXCEPT
#=================================================================================================

try:
    number = int(input("enter a number"))
    print(number)
except:
    print("invalid number")

# there are also specific exceptions - always use
try:
    number = int(input("enter a number"))
    print(number)
except ValueError:
    print("invalid number")

#=================================================================================================
# READING FILES
#=================================================================================================
# open file - can use filename or path.  open (filename, mode).
# mode "r" read, "w" write, "a" append,"r+" read & write  ( note:  use rU for universal read,it will always return \n on each line

# reading one line at a time in a for loop doesn't require the whole file to be in memory at once
f = open('foo.txt', 'rU')
for line in f:
    print(line,)   # trailing so print does not add end of line since there is already one on the line
f.close()

# f.readlines() reads the whole file in to memory and returns it's contents as a list of lines
# f.read() reads the whole file into a single string

#generally assigned to variable
open("filename.txt", "r")
employeeFile = open("employee.txt", "r")

# close file
employeeFile.Close()

# is file readable
print(employeeFile.readable())  # returns true or false; open must be mode r

# read
print(employeeFile.read())      # read whole file
print(employeeFile.readline())  # read one line
print(employeeFile.readlines())  # puts each line in an list
print(employeeFile.readlines()[1])  # access line 1

for empployee in employeeFile.readlines():
    print()

#=================================================================================================
# WRITING FILES
#=================================================================================================

employeeFile = open("filename.txt", "a")  # append
employeeFile.write("\nToby - HR")
employeeFile.Close()

# if file is open for write "w", adding a line will over write the entire file. use write to create a new file

#=================================================================================================
# MODULES
#=================================================================================================
# modules - a file to be included in to your current file (see Python Module Index)
# see External Libraries/Lib folder

import LinkedList
# syntax to use:    program1.<name of function>

#=================================================================================================
# PIP
#=================================================================================================
# pip - install external 3rd party modules
# bring up the DOS command window - pip should be there.  type: pip -- version    to check
# pip install moduleName
# goes to External Libraries/Lib/site packages folder

#=================================================================================================
# CLASSES AND OBJECTS
#=================================================================================================

class student:
    # initialize function
    def __init__(self, name, major, gpa, isOnProbation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.isOnProbation = isOnProbation

    # function\method
    def onHonorRoll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


# create a student object pretend if this is another file include the next line to import the class
# from student import student

student1 = student("Jim","Business",3.2, False)
print(student1.name)
print(student1.onHonorRoll)

# inheritance - create a second class that inherits all the functionality of the first class
#class chinesechef(chef):    chinesechef class inherits from chef class
