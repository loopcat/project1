import math
import operator
import re

#------------------------------------------------------------------------------------------
# compare two sets of triples
# input: 2 arrays each with 3 digits, one for each person
# output: 1 array with 2 elements, the score for each person
# logic:  if array1[i] > array2[i]  person1 gets one point
#         if array1[i] < array2[i]  person2 gets one point
#         if array1[i] = array2[i]  no points awarded
#
# Ex:  input: [5, 6, 7] and [3, 6, 10]   result: [1, 1]

def compare_triplets (list1, list2):
    person1Total, person2Total = 0, 0

    for i in range(3):
        if list1[i] > list2[i]:
            person1Total += 1
        if list1[i] < list2[i]:
            person2Total += 1

    result = []
    result.append(person1Total)
    result.append(person2Total)
    return result

list1 = [5, 6, 7]
list2 = [8, 6, 10]
#score = compare_triplets(list1, list2)
#print(score)


#------------------------------------------------------------------------------------------
# print the names of the people with the second to lowest scores, (names in alpha order if score the same)
# use a nested list [ (name,score), (name, score) ...].  There will always be one or more second lowest score
# input: Number of Students (n) and names/scores:
# 5
# name
# score
# name
# score ...
# output: Sally
#         Sam

def second_lowest_grade(n, name, score):
    # this didn't work need to use zip
    # grades = [(name,score) for name in ['Jane', 'Sally', 'Tom', 'Sam', 'Sara'] for score in [10,7, 5, 7, 10]]

    # in Python 3 zip returns an zip object which is an iterator so use 'list' if you want a list returned
    grades = list(zip(name, score))

    # sorts just by grade
    # grades.sort(key=operator.itemgetter(1))

    # sort the list by grade and name so people with the same score are in alpha order
    grades.sort(key= lambda x: (x[1], x[0]))

    # turn scores from list into set to get unique values and element 1 will be the 2nd lowest
    gradeSet = sorted(set([x[1] for x in grades]))
    secondLowest = gradeSet[1]
    [print(name)for name,score in grades if score == secondLowest]

# actual code used in Hackerrank IDE that works with their input
#if __name__ == '__main__':
#    grades = []
#    for _ in range(0, int(input())):
        # name = input()
        # score = float(input())
#        grades.append([input(), float(input())])

#    grades = list(zip(name, score))
#    grades.sort(key=lambda x: (x[1], x[0]))
#    lowestScore = grades[0][1]

#    for i in range(1, 4):
#      if grades[i][1] > lowestScore:
#            secondLowest = grades[i][1]
#            break

#    for i in range(1, 4):
#        if grades[i][1] == secondLowest:
#            print(grades[i][0])


#===================
name = ['Jane', 'Sam', 'Tom', 'Sally', 'Sara']
score = [10, 7, 5, 7, 8]
#second_lowest_grade(5, name, score)

#------------------------------------------------------------------------------------------
# reverse an array in place

def reverse_list(itemslist):
    start = 0
    end = len(itemslist) - 1

    while start < end:
        temp = itemslist[end]
        itemslist[end] = itemslist[start]
        itemslist[start] = temp
        start += 1
        end -= 1

#=================
items = [1, 2, 3, 4]
#reverse_list(items)
#print(items)

#---------------------------------------------------------------------------------------------
# given array of N elemenst sorted in non-decreasing order find if a number occurs more than half
# the number of elements in the array.  For ex: array of 10 elements, if a number occurs more than 5
# times it is the leader. Return -1 if no leader and leader if there is a leader

def find_leader(inputList):
    length = len(inputList) - 1
    half = length/2

    # create a set from the input list so we have the unique values in the list
    # then turn back in to list so we can use the count function
    listSet = set(inputList)
    uniqueList = list(listSet)

    uniqueLength = len(uniqueList)
    for i in range(uniqueLength):
        howmany = inputList.count(uniqueList[i])
        if howmany > half:
            return uniqueList[i]
    # no leader found
    return -1


#====================
inputlist = [8,8,8,8,10]
#leader = find_leader(inputlist)
#print(leader)

#------------------------------------------------------------------------------------

def e_index(inputList, n):
    sumLeft = 0
    sumRight = 0

    for i in range(0,n-1):
        # sum left side and sum right side then compare
        for j in range(0,i):
            sumLeft = sumLeft + inputList[j]
        for j in range(i+1, n):
            sumRight = sumRight + inputList[j]
        if sumLeft == sumRight:
            return i
        sumLeft = 0
        sumRight = 0

    return -1

#===================
inputList = [-1, 3, -4, 5, 1, -6, 2, 1]
#answer = e_index(inputList, 8)
#print(answer)

#--------------------------------------------------------------------
#Diagonal Difference - Given a matrix calc the sum of the diagnols and return the absolute value of the difference
# input n = number of rows/columns, arr = matrix
def diagonalDifference(n,arr):
    sum1 = sum(arr[i][i] for i in range(n))

    sum2 = 0
    for i in range(n):
        for j in range(n):
            if j == n - i - 1:
                sum2 = sum2 + arr[i][j]

    return abs(sum1 - sum2)

#--------------------------------------------------------------------
#PlusMinus - basically show decimal precision on print
# input: list of numbers, count the negative, positive and equal to 0 elements in the array and print the ratio
def plusMinus(arr):
    length = len(arr)
    negative = 0
    positive = 0
    zero = 0

    arr.sort()
    for i in range(length):
        if arr[i] < 0:
            negative = negative + 1
        if arr[i] == 0:
            zero = zero + 1
        if arr[i] > 0:
            positive = positive + 1

    print('%.6f' % (positive / length))
    print('%.6f' % (negative / length))
    print('%.6f' % (zero / length))

#--------------------------------------------------------------------
# Print Staircase - print precending spaces and a # for number of stairs at each level
# input n - the number of stairs
# ex:  n = 3   print:     #
#                        ##
#                       ###
#
def staircase(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(i + 1):
            print("#", end="")
        print()

#=====================
#staircase(5)

# --------------------------------------------------------------------
def time_conversion(timestring):

    # if PM and not noon just add 12 hours
    if timestring[-2:] == 'PM' and timestring[:2] != "12":
        hour = int(timestring[0:2])
        hour = hour + 12
        result = str(hour) + timestring[2:8]
        return result

    # noon just remove PM
    if timestring[-2:] == 'PM':
        return timestring[:-2]

    # check for midnight to 12:59, change hour to 00
    if timestring[-2:] == "AM" and timestring[:2] == "12":
        return "00" + timestring[2:8]

    # if AM and not midnight just remove AM
    if timestring[-2:] == "AM":
        return timestring[:-2]

#======================
#result = time_conversion("01:00:00PM")
#print(result)

# --------------------------------------------------------------------
#FizzBuzz problem:  For numbers 1 to n print number unless divisible by 3 then print 'Fizz',
#                   if divisible by 5 print 'buzz', if divisible by both 3 and 5 print 'FizzBuzz'

def FizzBuzz(n):

    for i in range(1,n+1):
        messageOut = ""

        if (i % 3) == 0:
            messageOut = "Fizz"
        if (i % 5) == 0:
            messageOut = messageOut + "Buzz"
        if messageOut == "":
            messageOut = str(i)
        print(messageOut)

#====================
#FizzBuzz(100)

# --------------------------------------------------------------------
#  Finding the Perentage - using dictionary data type
def find_percent():

    if __name__ == '__main__':
        n = int(input())
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()

# write code here
    if query_name in student_marks:
        scores = student_marks.get(query_name,[])
        ave = (scores[0] + scores[1] + scores[2])/3
        print('%.2f' % ave)

# --------------------------------------------------------------------
# Lists
def list_commands():
    if __name__ == '__main__':
        N = int(input())

    sampleList = []
    for i in range(N):
        inBuffer = input()
        command = inBuffer.split(" ")

        if command[0] == 'append':
            value = int(command[1])
            sampleList.append(value)
        elif command[0] == 'insert':
            index = int(command[1])
            value = int(command[2])
            sampleList.insert(index, value)
        elif command[0] == 'pop':
            sampleList.pop()
        elif command[0] == 'print':
            print(sampleList)
        elif command[0] == 'remove':
            value = int(command[1])
            sampleList.remove(value)
        elif command[0] == 'reverse':
            sampleList.reverse()
        elif command[0] == 'sort':
            sampleList.sort()

# --------------------------------------------------------------------
# find all occurances of a substring
def count_substring(string, sub_string):
    count = 0
    x = len(sub_string)

    for i in range(0, len(string) - x + 1):
        endIndex = (i + x)
        if (string.find(sub_string,i,endIndex) > -1):
            count += 1
    return count
# --------------------------------------------------------------------
#newString = "cat in the cat hat cat"
#sub = "cat"
#print(newString.find(sub,19))

# --------------------------------------------------------------------
# Designer Door Mat  (hackerrank read from stdin, use function here)
def door_mat(r,c):

    #r, c = input().split()
    rows = int(r)
    cols = int(c)

    welcome = 'WELCOME'
    designString = '.|.'
    rowsBeforeAfter = rows//2
    mid = cols//2

    # print rows before the Welcome row
    for i in range(rowsBeforeAfter):
        print((designString*i).rjust(mid-1,'-') + designString + (designString*i).ljust(mid-1,'-'))

    # print Welcome row
    print(welcome.center(cols,'-'))

    # print rows after Welcome
    for i in range(rowsBeforeAfter-1,-1, -1):
        print((designString*i).rjust(mid-1,'-') + designString + (designString*i).ljust(mid-1,'-'))

#======================
#door_mat(7,21)

# --------------------------------------------------------------------
# String Formatting - printing decimal, octal, hex and binary numbers right justified by length of binary number
def print_formatted(number):
    binaryString = "{:b}".format(number)
    l = len(binaryString)

    for i in range(1,number+1):
        print(("{:d}".format(i)).rjust(l), ("{:o}".format(i)).rjust(l), ("{:X}".format(i)).rjust(l),("{:b}".format(i)).rjust(l))
#======================
#print_formatted(10)

# --------------------------------------------------------------------
# Alphabet Rangoli

def print_rangoli(size):
    # setup alphabet list
    alphaList = ['1','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # calc number of rows and width of design
    rows = 2*(size-1) + 1
    width = size + (size-1) + 2*(size-1)
    half = int((width-1)/2)

    # print first half
    leftString = ''
    for i in range(size):
        # build left string
        for j in range(i):
            leftString = leftString + alphaList[size-j] + '-'

        # right string reverse of left
        rightString = "".join(reversed(leftString))

        print((leftString.rjust(half,'-')) + alphaList[size-i] + (rightString.ljust(half,'-')))
        leftString = ''

    # print second half
    for i in range(size-2,-1,-1):
        for j in range(i):
            leftString = leftString + alphaList[size-j] + '-'

        rightString = "".join(reversed(leftString))

        print((leftString.rjust(half,'-')) + alphaList[size-i] + (rightString.ljust(half,'-')))
        leftString = ''
#======================
#print_rangoli(5)

# --------------------------------------------------------------------
# capitalize the first char of each word only if word starts with a character, ignore if alphanumberic

def solve(s):
    words = s.split(' ')
    newString = [i.capitalize() for i in words]
    result = " ".join(newString)
    return result

# --------------------------------------------------------------------
# Minion game with strings

def minion_game1(s):
# bad code but contains some examples on how to use string functions
    vowels = 'AEIOU'
    inputLen = len(s)
    score1 = 0
    score2 = 0
    newSubstring = ''
    stringList1 = []
    stringList2 = []

    for i in range(inputLen):
        if s[i] in vowels:
            for j in range(i,inputLen):
                newSubstring = newSubstring + s[j]    # add to substring
                if newSubstring not in stringList1:   # if new substring score it
                    stringList1.append(newSubstring)      # add new substring to list for player1
                    repeats = len(re.findall(r'(?=(' + newSubstring + '))',s))   # how many occurances of substring
                    score1 += repeats
            newSubstring = ''
        else:
            for j in range(i,inputLen):
                newSubstring = newSubstring + s[j]
                if newSubstring not in stringList2:
                    stringList2.append(newSubstring)
                    repeats = len(re.findall(r'(?=(' + newSubstring + '))', s))
                    score2 += repeats
            newSubstring = ''
    if score1 > score2:
        print('Kevin ',score1)
    else:
        print('Stuart ', score2)

def minion_game2(s):
    vowels = 'AEIOU'
    instringLen = len(s)
    score1 = 0
    score2 = 0

    for i in range(instringLen):
        if s[i] in vowels:
            score1 += instringLen - i
        else:
            score2 += instringLen - i

    if score1 > score2:
        print('Kevin',score1)
    elif score2 > score1:
        print('Stuart', score2)
    else:
        print('Draw')

#======================

#minion_game2('BANANA')

# --------------------------------------------------------------------
# Merge the Tools (substrings and removing dup characters)

def merge_the_tools(string, k):
    # your code goes here
    lenString = len(string)
    i = 0
    set1 = set()
    list1 = []

    while i < lenString:
        newSub = string[i:i+k]
        for ch in newSub:
            if ch not in set1:
                list1.append(ch)
                set1.add(ch)
        print(''.join(list1))
        list1 = []
        set1 = set()
        i += k

merge_the_tools('AABCAAADA',3)

# --------------------------------------------------------------------
# Introduction to sets - add input items to set and sum, then divide by number of items
def average(array,n):
    set1 = set()

    for i in range(n):
        set1.add(array[i])

    sumHeights = sum(set1)
    numItems = len(set1)
    return sumHeights / numItems

#average([161, 182, 161, 154, 176, 170, 167, 171, 170,174],10)