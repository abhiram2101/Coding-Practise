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
"""
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
