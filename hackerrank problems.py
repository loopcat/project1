import math
import operator

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