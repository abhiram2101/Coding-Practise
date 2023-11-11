lis = [ 1,2,3,1,2,5,9,6,1,3,4]
res ={}
for ele in lis :
    if ele in res :
        res[ele] +=1
    else :
        res[ele] = 1
print(res)

