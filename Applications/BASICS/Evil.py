def count_one(n):
    c_one = 0
    while n != 0:
        rem = n % 10
         
        if rem == 1:
            c_one = c_one + 1
        n = n // 10
         
    return c_one

def checkEvil(n):
    i = 0
    binary = 0
     
    while n != 0:
        r = n % 2
        binary = binary + r*(int(10**i))
        n = n // 2

    n_one = count_one(binary)
    if n_one % 2 == 0:
        return True
    return False
     
num = int(input("Enter Number : "))
check = checkEvil(num)

if check:
    print("{0} - Is An Evil Number".format(num))
else:
    print("{0} - Is An Odious Number".format(num))