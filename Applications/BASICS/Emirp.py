def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solve(num):
    if not is_prime(num):
        return False
    reverse_num = 0
    while num != 0:
        d = num % 10
        reverse_num = reverse_num * 10 + d
        num = int(num / 10)
    return is_prime(reverse_num)

n = int(input("Enter Number : "))
if solve(n) == True:
    print("{0} - Is An Emirp Number".format(n))
    
else:
    print("{0} - Is Not An Emirp Number".format(n))