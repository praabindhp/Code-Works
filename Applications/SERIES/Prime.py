n = int(input("Enter The Number Of Values : "))
res = []
for i in range(2,n):
        if(n%i == 0):
            res.append(n)