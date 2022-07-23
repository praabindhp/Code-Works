n = int(input("Enter The Number Of Values : "))
prod = 0
res = []
for i in range(1, n+1):
    prod += i
    res.append(prod)

print(*res)