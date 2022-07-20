import math

def magicNum(n):
    digitCount = int(math.log10(n))+1
    sumOfDigits = 0

    temp = n
    while( digitCount > 1):

        sumOfDigits = 0

        while(temp > 0):
            sumOfDigits += temp%10
            temp = temp//10

        temp = sumOfDigits

        digitCount = int(math.log10(sumOfDigits))+1
    
    if(sumOfDigits == 1):
        print("{0} - Is A Magic number".format(n))
        
    else:
        print("{0} - Is Not A Magic Number".format(n))
        
n = int(input("Enter A Number : "))
magicNum(n)