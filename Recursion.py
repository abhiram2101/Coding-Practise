"""# python3 program to print 1 to n using recursion

def printNumber(n):
  # check if n is greater than 0
  if n > 0:
    # recursively call the printNumber function
    printNumber(n - 1)
    # print n
    print(n, end = ' ')

# declare the value of n
n = 50
# call the printNumber function
printNumber(n)

#printing names N times using recursion
def printn(n,i) :
    if i==0:
        return
    print(n)
    printn(n,i-1)
n =input()
printn(n,5)
"""
#printing names N-1 times using recursion
def printn(n,i) :
    if i>5:
        return
    print(n)
    printn(n,i+1)
n =input()
printn(n,1)
