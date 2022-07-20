def isPalindrome(s):
    return s == s[::-1]

n = input("Enter String : ")
s = n.lower()

ans = isPalindrome(s)

if ans:
    print("{0} - Is Palindrome".format(n))
else:
    print("{0} - Is Not A Palindrome".format())