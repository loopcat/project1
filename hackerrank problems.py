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
score = compare_triplets(list1, list2)
print(score)


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
second_lowest_grade(5, name, score)