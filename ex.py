t = int(input("enter len of the list"))
lis = []
n = int(input("enter a number to search"))
for i in range(t):
    x= int(input())
    lis.append(x)
print(lis)
z=len(lis)
print(z)
for i in range(z):
        if i == n :
            print("found",i)
        else :
            print("not found")



    


