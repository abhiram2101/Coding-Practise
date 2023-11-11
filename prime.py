
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    ans = isPrime(n)
    if n != 1 and ans == True:
        print("Prime Number")
    else:
        print("Non Prime Number")
    print("Prime numbers below",n,"are :")
    for i in range(2,n+1) :
        if isPrime(i) :
            print(i,end=" ")



