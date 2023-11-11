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
