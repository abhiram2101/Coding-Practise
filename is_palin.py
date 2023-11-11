def is_palin(n) :
    s2= n[ ::-1]
    if n == s2 :
        print("yes",n, "is palindrome")
    else :
        print("no",n, "is not a palindrome")
n=input()
is_palin(n)
