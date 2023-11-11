"""class dog:
	def __init__(self,hgt,clr):
		self.hgt = hgt
		self.clr = clr
dog("tall" , "white")
print(dog.hgt)

n = int(input())
arr = map(int, input().split())
def find_s(arr):
    s = sorted(arr)
    b =set(s)
    ind = max(s)
    b.remove(ind)
    print(max(b))
find_s(arr)

n=int(input())
    for i in range(n):
        name = input()
        score = float(input())

fin_lis=[]
temp_lis = []
n=int(input())
for i in range(n):
    for j in range(1):
        name = input()
        score = float(input())
        temp_lis.append(name)
        temp_lis.append(score)
    fin_lis.append(temp_lis)
print(fin_lis)


for a in my_list:
    for b in my list:
        if a[1] > b[1] :
            print(b[0])
        else :

        for z in my_list:
    ind = max(my_list[1])
    print(ind)
my_list.remove(ind)
print(my_list)

for y in temp:

my_list.remove(ind)
print(my_list)
ind = min(jth)
print(ind)


        if ith == min(jth):

my_list = []
temp_list = []
n = int(input('Enter the number of sub-lists: '))
for i in range(n):
    #for j in range(2):
    temp_list.append(input())
    my_list.append(temp_list)
    temp_list = []
print(my_list)
#temp = sorted(my_list)
#print(temp)
maxy=[]
for ith in my_list:
    for jth in my_list:
        maxy.append(jth[0])
    maxy = []
print(maxy)
marks = []
namemarks = []
for i in range(int(input())):
        name = input()
        score = float(input())
        marks.append(score)
        namemarks.append([name,marks])
s = sorted(set(marks))
sec_low = s[1]
namemarks.sort()
for ele in namemarks :
    if ele[1]==sec_low :
        print(ele[0])
         for j in lis:
                if j == min(lis):
                        lis1.append(j)
                        lis.remove(j)
                        lis.remove(lis[0])
                
                else:
                        lis.remove(lis[0])
        print(lis)
        print(lis1)
print(lis)
print(lis1)

lis = [6,4,9,10,34,56,54]
lis1 = []
lis2= []
for i in lis :
        lis2.append(i)
        if i=
        =min(lis) :
                lis1.append(i)
                lis2.remove(i)
                print(lis)
                print(lis1)
                print(lis2)
        
        else :
                for k in lis2 :
                        lis2.pop()

       


arr = [7,9,4,3,2]
k = 3
ind = [0 , 3]
def main(arr,k,ind) :
    n=len(arr)
    def rotate(arr) :
        last = arr[-1]
        print(last)
        for i in range(n-1,0,-1) :
            arr[i] = arr[i-1]
            print("every array",arr)
        arr[0] = last
        print("final arr",arr)
    for i in range(k) :
        rotate(arr)
    res = [arr[i] for i in ind]
    return res
res = main(arr, k, ind)
print(res)




s=input()
rev_str =s[::-1]
lis=[]
for i in rev_str :
    if i =="G" :
        lis.append("C")
    elif i == "C" :
        lis.append("G")
    elif i=="T" :
        lis.append("A")
    elif i == "A" :
        lis.append("T")
for i in lis:
    print(i,end="")


from collections import defaultdict
dict =defaultdict(list)
print(dict)


s ="PPPPPP@PPP@PP$PP"
groups = s.split("$")
print(groups)
min_length = float('inf')
for group in groups :
    subgroups = group.split("@")
    print(subgroups)
    length = [len(subgroup) for subgroup in subgroups]
    min_length = min(min_length,min(length))
    print(min_length)



def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  while number % 2 == 0:
    number = number // 2
    print(number)
    continue
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  if number == 1:
    return True
  return False
print(is_power_of_two(9))



"""
for x in range(10):
    for y in range(x):
        print(y)


















