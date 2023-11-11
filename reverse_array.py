"""
#iterative method
def reverse(arr,n) :
    arr2= []
    for i in range(n,0,-1):
        arr2.append(i)
        #print(i)
    print(arr2)
arr = [1,2,3,4,5]
n=len(arr)
reverse(arr,n)

# time complexity is O(n) because traverse through N elements
# space complexity is O(n) becaues extra array is used

#using recursion approach
def reverse(arr,start_ind , end_ind) :
    if start_ind < end_ind :
        arr[start_ind] ,arr[end_ind] = arr[end_ind] , arr[start_ind]
        reverse(arr,start_ind +1 , end_ind-1)
        print(arr)
arr = [1, 2, 3, 4, 5] #you can also change code to take input array dynamically
n=len(arr)
print(reverse(arr,0,n-1))

  
"""
# using two pointer approach 
def  reverse(arr,n) :
    p1=0
    p2=n-1
    while p1<p2 :
        arr[p1],arr[p2] = arr[p2] ,arr[p1]
        p1 += 1
        p2 -= 1
    return(arr)
arr = [5, 4, 3, 2, 1]
n =len(arr)
print(reverse(arr,n))
