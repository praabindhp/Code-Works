nterms = int(input("Enter Number Of Terms : "))

n1, n2 = 0, 1
count = 0
res = []

if nterms <= 0:
   print("Please Enter A Valid Positive Integer")
elif nterms == 1:
   print("Fibonacci Sequence Upto",nterms,":")
   print(n1)

else:
   print("Fibonacci Sequence:")
   while count < nterms:
       res.append(n1)
       nth = n1 + n2

       n1 = n2
       n2 = nth
       count += 1

print(*res)