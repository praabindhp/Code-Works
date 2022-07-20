def primeComposite(n):
    
    if(n ==0 or n == 1):
        print("{0} - Is Neither Prime Nor Composite".format(n))
        
    elif n>1 :
        for i in range(2,n):
            if(n%i == 0):
                print("{0} - Is A Composite Number".format(n))
                break
        else:
            print("{0} - Is A Prime Number".format(n))
    else :
        print("Please Enter Positive Number Only !")
        
n = int(input("Enter Number : "))
primeComposite(n)