def findarr(A):
    A.sort()
    print(A)
    arrlis=[]
    for i in range(len(A)+1):
        if i>0:
            arrlis.append(i)
    for res in range(len(A)+1):
        if i<0:
            return 1
        elif i>1:
            for ele in arrlis:
                if ele in A:
                    pass
                else:
                    return ele
            
           
                
        




print(findarr([1,3,6,4,7]))

#[1,2,1,3,4]            [-1,-3]  [1,3,6,4,7]

"""
d={}
    genlis=[]
    out={}
    highEle = A[-1]
    print(highEle)
    
    for ele in A:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    #return d
    for j in range(1,highEle+1) :
        genlis.append(j)
    #return genlis
    for k in d.keys():
        if k in genlis:
            pass
        else:
            print("else")
            return genlis[k]

            """
