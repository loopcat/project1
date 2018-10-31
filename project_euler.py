import math
import fractions

# -------------------------------------------------------------------------------------------------------------
# prime factorization of a number n
# ex:  12 --> 2, 2, 3
#      147 --> 3, 7, 7
#      17 --> 17
#      13195 --> 5, 7, 13, 29


def prime_factorization(n):
    isEven = True

    # divide by smallest prime - 2 for as long as possible
    while isEven:
        if n % 2 == 0:
            print(2, end=" ")
            n = n / 2
        else:
            isEven = False

    # at this point n is odd, start factoring with 3 and increase by 2
    sqroot = int(math.sqrt(n))
    for i in range(3,sqroot,2):
        if n % i == 0:
            print(i, end = " ")
            n = n / i

    # n is prime number greater than 2
    if n > 2:
        print(int(n))

#=====================================
#print("prime factorization of 600851475143")
#prime_factorization(600851475143)
prime_factorization(20)



# -------------------------------------------------------------------------------------------------------------
# find the largest palindrome from the product of two 3 digit numbers
# ex:  the largest palindrome from the product of two 2 digit numbers is 9009  (91 x 99)

def find_palindrome():
    palindromeList = []

    for i in range(100,1000):
        for j in range(i,1000):
            result = i * j

            # check if result is a palindrome - convert to strings then lists, reverse and compare
            string1 = str(result)
            list1 = list(string1)
            list2 = list1.copy()
            list2.reverse()

            # compare if two lists are the same
            if list1 == list2:
                if result not in palindromeList:
                    palindromeList.append(result)

    # sort final list and print largest palindrome
    palindromeList.sort(reverse=True)
    print(palindromeList[0])

#===================
#find_palindrome()













