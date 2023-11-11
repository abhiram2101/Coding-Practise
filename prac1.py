"""

Nlist = [1,2,2,1,3,7,12,16,21,12,45]

Mlist = [1,2,7,12,3]

#arrange Nlist elements ac to Mlist positions if elements are not there then 
# arrange them in increasing order.

newlist=sorted(Nlist)
print(newlist)
"""
lis1 = []
lis2 = []
resu=[]
Ntotal = int(input())
for ele in range(Ntotal) :
    ele = int(input())
    lis1.append(ele)
#print(lis1)
Mtotal=int(input())
for ele1 in range(Mtotal) :
    ele1 = int(input())
    lis2.append(ele1)
#print(lis2)
for i in lis2 :
    if i in lis1:
        resu.extend([i] * lis1.count(i))
remaining_elements = [element for element in lis1 if element not in lis2]
resu.extend(sorted(remaining_elements))
print(resu)
"""
for i in resu :
    print(i,end=", ")
"""
