import numpy as np

# given an input list of integers, treat as a number and add 1  Ex:  [1,2,3,5] --> 1,235 + 1 = 1,236
def add_one(input_num):
    # new array same size of input list to hold the answer
    result = np.zeros(len(input_num))

    carry = 1
    sum = 0

    for i in range ((len(input_num) - 1), -1, -1):
        sum = input_num[i] + carry
        if sum == 10:
            carry = 1
        else:
            carry = 0

        result[i] = sum % 10

    # check for edge cases 999 --> 1000
    if carry == 1:

        # create new array one larger and init to zeros
        length = len(input_num) + 1
        new_result = np.zeros(length)
        new_result[0] = 1

        return new_result
    else:
        return result
# end of function

# calls to add_one
input_num = [1,3,4,5]
answer = add_one(input_num)
print(answer)
input_num = [9,9,9]
answer = add_one(input_num)
print(answer)
