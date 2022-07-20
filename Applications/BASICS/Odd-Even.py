def evenOdd(n):
    if (n % 2) == 0:
        print("{0} - Is Even".format(n))
    
    else:
        print("{0} - Is Odd".format(n))
   
n = int(input("Enter Number : "))
evenOdd(n)