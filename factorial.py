"""
# using recursion
def fact_recursive(n) :
    if n==0:
        return 1 # factorial of 0 is "1"
    return n*fact_recursive(n-1)
n = int(input())
print(fact_recursive(n))

"""
#using iterative method
def fact(n) :
    res = 1
    for i in range(1,n+1) :
        res = res*i
    return res
n=int(input())
print(fact(n))


