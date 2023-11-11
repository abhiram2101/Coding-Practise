"""
#if the input is integer ( time coplexity is O(n), space coplexity is O(1)
n = int(input())
reverse_num = 0
while n!=0 :
    digit = n%10
    reverse_num = reverse_num *10 + digit
    n = n//10
print("reverse of num is ",reverse_num)

#if the input is string (
n = input()
print(n[::-1])
#print("reverse of num is ",reverse)

#time coplexity is O(n)

"""
#by type casting from int to str

n=str(int(input()))
print(n[::-1])
