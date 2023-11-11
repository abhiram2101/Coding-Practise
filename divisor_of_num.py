def divisor(n) :
    for i in range(1,n+1) :
        if n%i == 0 :
            print(i)
        else:
            pass
n = int(input())
divisor(n)
#time complexity is O(n) as we need to traverse for n elements

#optimal solution in notebook and below 

"""

def printDivisorsOptimal(n):
    print("The Divisors of",n,"are:")
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            print(i, end=" ")
            if i != n/i:
                print(int(n/i), end=" ")#printing divisor and questiont as the result of both is 'n'
    #print()
if __name__ == "__main__":
    printDivisorsOptimal(126)

#Time Complexity: O(sqrt(n)), because every time the loop runs only sqrt(n) times.
"""
