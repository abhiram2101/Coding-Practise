#code to find sum of N natural number  
"""
# using recursion
def recursive(n) :
    if n==0:
        return 0
    return n+recursive(n-1)
n = int(input())
print(recursive(n))


#using iterative method

sum = 0
n=int(input())
for i in range(1,n+1) :
    print(i,end=" ")
    sum += i
print(end="\n")
print(sum)
"""
def sumn(n) :
    if n == 0 :
        return o
    return n*(n+1)//2
    #print(res)
n = int(input())
print(sumn(n))

