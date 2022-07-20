def reverse(x):
     
    rev = 0;
    while (x > 0):
        rev = (rev * 10) + x % 10;
        x = int(x / 10);
 
    return rev;
 
def printEmirp(n):
    prime = [1] * (n + 1);
    p = 2;
    while (p * p <= n):
         
        if (prime[p] == 1):
             
            for i in range(p * 2, n + 1, p):
                prime[i] = 0;
        p += 1;

    for p in range(2, n + 1):
        if (prime[p] == 1):
             
            rev = reverse(p);
 
            if (p != rev and rev <= n and
                       prime[rev] == 1):
                print(p, rev, end = " ");

                prime[rev] = 0;

n = int(input("Enter The N Value : "))
printEmirp(n);