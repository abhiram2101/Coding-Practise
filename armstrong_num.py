import math
from math import *
def check_arm(n) :
    org_num = n
    temp = n
    count = 0
    while temp!=0 :
        count += 1
        temp //= 10
    power = 0
    while n!=0 :
        digit = n%10
        power += pow(digit,count)
        n//=10
    return power == org_num
if __name__ == "__main__" :
    n = int(input())
    if check_arm(n) :
        print("yes")
    else :
        print("no")   
#time complexity is O(n) and space complexity is O(1)
