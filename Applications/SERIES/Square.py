n = int(input("Enter The Number Of Values : "))
res = []
for i in range(1, n+1):
    res.append(i**2)
    
print(*res)