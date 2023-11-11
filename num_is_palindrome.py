"""
#if the input is number
# we will check if the given number and the reversed number is equal or not
# I did modules to get the last digit of the number and add it to another variable i.e "reverse_num"
"""
def check_palin(n) :
    reverse_num = 0
    num = n
    while n!=0 :
        digit = n%10
        reverse_num = reverse_num*10 + digit
        n = n//10
    print(reverse_num)
    if num == reverse_num :
        print(num ,"is palindrome")
    else :
        print(num ,"is not a palindrome")
n = int(input())
check_palin(n)
#Time Complexity: O(logN) for reversing N digits of input integer.

#Space Complexity: O(1)
