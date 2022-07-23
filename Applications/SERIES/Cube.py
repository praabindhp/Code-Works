n = int(input("Enter The Number Of Values : "))
res = []
for i in range(1, n):
    res.append(i**3)
    
print(*res)