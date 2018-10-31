# input:  a list of 8 integers (only 1's and 0's) and number of days
# a 0 is assumed as a prefix to the list and a 0 is assumed as the 9th element
# if the neighbors on either side of an element are the same the element is given the value 0  else value 1

# Test Case 1:  0 [1,0,0,0,0,1,0,0] 0    1 day
# result:         [0,1,0,0,1,0,1,0]

# Test Case 2:  0 [1,1,1,0,1,1,1,1] 0    2 days
# result:         [0,0,0,0,0,1,1,0]

def new_status (inputList, n):
    # init result list
    result = [0,0,0,0,0,0,0,0]

    for days in range (n):
        for i in range (0,8):
            # special case first and last element in list
            if i == 0:
                if inputList[1] == 0:
                    result[0] = 0
                else:
                    result[0] = 1
            elif i == 7:
                if inputList[6] == 0:
                    result[7] = 0
                else:
                    result[7] = 1
            else:
                if inputList[i-1] == inputList[i+1]:
                    result[i] = 0
                else:
                    result[i] = 1

        # copy result list to inputList for next day (but keep them as seperate lists)
        inputList = result[:]

    return result

# ********************

# test case 1
input = [1,0,0,0,0,1,0,0]
print("Input List: ", input)
answer = new_status(input,1)
print("Result:     ", answer)

# test case 2
input = [1,1,1,0,1,1,1,1]
print("Input List: ", input)
answer = new_status(input,2)
print("Result:     ", answer)





