def fact(n):
    
    factorial = 1
    if n < 0:
        print("Sorry, factorial does not exist for negative numbers")

    elif n == 0:
        print("The factorial of 0 is 1")

    else:
        for i in range(1,n + 1):
            factorial = factorial*i
        print("{0} Factorial Is - {1}".format(n, factorial))
    
n = int(input("Enter Number : "))
fact(n)