
def gcd_num(num1,num2) :
    temp=[]
    min_num = min(num1,num2)
    #print(min_num)
    for i in range(1,min_num+1) :
        if num1%i ==0 and num2%i ==0 :
            #print(i)
            temp.append(i)
        else :
            pass
    #print(temp) #[1,2,4]
    res = max(temp)#[4]
    print(res)#[4]
num1= int(input())
num2 =int(input())
gcd_num(num1,num2)
"""
#Time Complexity: O(N)
#now let us look at optimal approach using Euclidean theorem
import math
from math import *
def gcd_num (a,b) :
    if b==0 :
        return a
    return gcd(b,a%b)
a = int(input())
b = int(input())
print(gcd_num(a,b))

#space complexity is O(1)

"""

















#now let us look at optimal approach using recurssion
