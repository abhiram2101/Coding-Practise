"""
arr = [1,2,3,4,5]
n = 5
s =5
#for i in range(n) :
    #arr.append(i.split(" "))
#print(arr)
lis = []
for i in range(len(arr)) :
    for j in range(len(arr)) :
        if arr[i] + arr[j] == s and arr[i] <= arr[j] :
            #print(arr[i],arr[j])
            #lis.append(arr[i])
            #lis.append(arr[j])
            pair = [0 for i in range(2)]
            pair[0] = arr[i]
            pair[1] = arr[j]
            lis.append(pair)
for i in range(len(lis)) :
    print(lis[i][0],lis[i][1])
        


def pairSum(Arr,s):
    n = len(arr)
    map = OrderedDict()
    ans - []
    for num in arr :
        map[num] =map.get(num,o)+1
    keyArray = sorted(map.key())
    for key in keyArray:
        if key+key = s  :
            freq = map[key]
            for j in range(freq*(freq-1)//2) :
                ans.append([key,key])
    low = 0
    high = len(keyArray)-1
    while(low<high) :
        currSum = keyArray[low] + keyArray[high]
        if currSum == s :
            freq = map[keyArray[low]] * map[keyArray[high]]
            for j in range(freq) :
                ans.append([keyArray[low],keyAray[high]])
            low = low +1
            high =high -1
        elif currSum < s :
            low = low+1
        else :
            high = high -1
    for i in range(len(ans)) :
        a =ans[i][0]
        a = ans[i][1]
        ans[i][0] = min(a,b)
        ans[1][1] = max(a,b)
    ans = sorted(ans,keys=lambda x :x[0])
    return ans



arr = [1,2,3,4,5,6]
n = 6
k =3
#for i in range(n) :
    #arr.append(i.split(" "))
#print(arr)
lis = []
for i in range(len(arr)) :
    for j in range(len(arr)) :
        if (arr[i] + arr[j]) / k ==0 and arr[i] <= arr[j] :
            #print(arr[i],arr[j])
            #lis.append(arr[i])
            #lis.append(arr[j])
            pair = [-1 for i in range(2)]
            pair[0] = arr[i]
            pair[1] = arr[j]
            lis.append(pair)
#for i in range(len(lis)) :
    #print(lis[i][0],lis[i][1])
    print(lis)
print(len(lis))

def count(n) :
    x=n
    c=0
    while(x!=0) :
        x//=10
        c+=1
    print(c)
n=123
count(n)

import math
from math import *
def count(n) :
    res = math.floor(log10(n)+1)
    print(res)
n=123
count(n)



def reverselis(n):
    for i in n :
        res =i%10
        print(res)
n = int(input())
reverselis(n)


lis = [[('key3', 800)], [('mani', 22)], [], [], [('abhi', 25), ('key7', 600)], [], [], [], [], [('kumari', 45)], [], [], [], [], [], [], [], [], [('key1', 100)], []]
for u in lis :
    for v in u :
        print(v)
    


#<-- finding min of element without usiing min fun -- >

lis = [1,-1,-2,-5,-3]
low = lis[0]
def ret(lis,low) :
    for i in lis :
        if low > i :
            low = i
    return low
print(ret(lis,low))


#<-- finding max of element without usiing max fun -- >


lis1 = [1,5, -2 , 6 , 40]
high = lis[0]
def ret(lis1,high) :
    for i in lis1 :
        if high < i :
            high = i
    return high
print(ret(lis1,high))


"""
#<-- finding max element in a list using linear search with for loop (unordered list) -- >
def iter() :
    lis1 = [2,43,4,1,12,45,0,7,9]
    #low = lis1[0]
    #high = lis1[-1]
    temp = 0
    for i in range(len(lis1)) :
        for j in range(len(lis1)) :
            print(lis1[i],end=" ")
            print(lis1[j])
            if lis1[i] < lis1[j] : # if the second element is bigger than first ele then swap
                # in the first loop i is 2 and j is 2,
                # in second loop i is 2 and j is 43 so it swap
                #print("executed",lis1[i])
                temp = lis1[j]
                lis1[j] = lis1[i]
                lis1[i] = temp
                print("swapped {} , {} ".format(lis1[i],lis1[j]))
                print(lis1)
                #print("{} th loop over" .format(j))
                
    print("min is {}".format(lis1[0]))
    print("max is {} ".format(lis1[-1]))
    return lis1
print(iter())









