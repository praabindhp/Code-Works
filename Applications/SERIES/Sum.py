n = int(input("Enter Number Of Terms : "))
sum = 0
res = []
for i in range(1, n+1):
    sum = sum+i
    res.append(sum)
    
print(*res)