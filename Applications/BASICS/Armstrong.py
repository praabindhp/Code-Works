def amstrong(n):
    sum = 0

    # find the sum of the cube of each digit
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    # display the result
    if n == sum:
        print("{0} - Is An Armstrong Number".format(n))
        
    else:
        print("{0} - Is Not An Armstrong Number".format(n))
        
n = int(input("Enter Number : "))
amstrong(n)