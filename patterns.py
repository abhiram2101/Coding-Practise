"""
def pattern():
    n = int(input())
    for i in range(n+1,0,-1) :
        for k in range(i,n+1) :
            print(end=" ")
        for j in range(i) :
            print("*",end=" ")
        for z in range(i, n+1) :
            print(end=" ")
        print(end="\n")
pattern()

def pattern():
    n = int(input())
    for i in range(n+1) :
        for k in range(i,n) :
            print(end=" ")
        for j in range(i) :
            print("*",end=" ")
        for z in range(i, n) :
            print(end=" ")
        print(end="\n")
pattern()

def pattern3() :
    n= int(input())
    for i in range(n,0,-1) :
        for j in range(i) :
            print(i,end="")
        print(end="\n")
pattern3()


def pattern4() :
    j=1
    n= int(input())
    for i in range(n,0,-1) :
        for j in range(i) :
            print(i,end="")
        print(end="\n")
pattern4()


def pattern5() :
    i=1
    j=1
    n= int(input())
    for i in range(n+1,0,-1) :
        for j in range(1,i) :
            print("*",end="")
        print(end="\n")
pattern5()

def pattern6() :
    i=1
    j=1
    n= int(input())
    for i in range(n+1,0,-1) :
        for j in range(1,i) :
            print(j,end="")
        print(end="\n")
pattern6()



def pattern7() :
    n= int(input())
    for i in range(1,n+1) :
        for j in range(1,i+1) :
            print(i,end="")
        print(end="\n")
pattern7()



def pattern8() :
    n= int(input())
    for i in range(1,n+1) :
        for j in range(1,i+1) :
            print(j,end="")
        print(end="\n")
pattern8()


def pattern9() :
    n = int(input())
    print(end="")
    for i in range(n+1) :
        for k in range(i,n+1) :
            print(end=" ")
        for j in range(i) :
            print("*",end=" ")
        for z in range(i, n+1) :
            print(end=" ")
        print(end="\n")
    for i in range(n+1,0,-1) :
        for k in range(i,n+1) :
            print(end=" ")
        for j in range(i) :
            print("*",end=" ")
        for z in range(i, n+1) :
            print(end=" ")
        print(end="\n")
pattern9()




def pattern10() :
    n = int(input())
    print(end="")
    for i in range(n+1) :
        #for k in range(i,n+1) :
            #print(end=" ")
        for j in range(i) :
            print("*",end=" ")
        #for z in range(i, n+1) :
            #print(end=" ")
        print(end="\n")
    for i in range(n+1,0,-1) :
        #for k in range(i,n+1) :
            #print(end=" ")
        for j in range(i) :
            print("*",end=" ")
       # for z in range(i, n+1) :
            #print(end=" ")
        print(end="\n")
pattern10()

def pattern11() :
    n = int(input())
    print(end="")
    for i in range(n+1) :
        #for k in range(i,n+1) :
            #print(end=" ")
        for j in range(i) :
            print("*",end="")
        #for z in range(i, n+1) :
            #print(end=" ")
        print(end="\n")
    for i in range(n+1,0,-1) :
        #for k in range(i,n+1) :
            #print(end=" ")
        for j in range(i) :
            print("*",end="")
       # for z in range(i, n+1) :
            #print(end=" ")
        print(end="\n")
pattern11()


def pattern12() :
    start=1
    n= int(input())
    for i in range(n+1):
        if i%2==0 :
            start =0
        else:
            start=1
        for k in range(0,i):
            print(start,end="")
            start = 1-start
        print(end="\n")
pattern12()


import string
def pattern13() : 
    upper = list(string.ascii_uppercase)  
    #print(upper)  
    n = int(input())
    for i in range(0,n+1) :
        for j in range(0,i) :
            print(upper[j],end=" ")
        print(end="\n")
pattern13()


import string
def pattern14() : 
    upper = list(string.ascii_uppercase)
    n = int(input())
    for i in range(n+1) :
        for j in range(i) :
            print(upper[i],end=" ")
        print(end="\n")
pattern14()



import string
def pattern15() :
    upper = list(string.ascii_uppercase)
    n = int(input())
    for i in range(n-1,0-1,-1) :
        for j in range(i+1) :
            print(upper[i],end=" ")
        print(end="\n")
pattern15()

import string
def pattern15() :
    upper = list(string.ascii_uppercase)
    n = int(input())
    for i in range(n-1,0-1,-1) :
        for j in range(i+1) :
            print(upper[j],end=" ")
        print(end="\n")
pattern15()


import string
def pattern16() :
    upper = list(string.ascii_uppercase)
    n = int(input())
    for i in range(n) :
        for j in range(i+1) :
            print(upper[i],end="")
        print(end="\n")
pattern16()


import string
def pattern17() :
    upper = list(string.ascii_uppercase)
    n = int(input())
    for i in range(n+1) :
        for k in range(i,n+1) :
            print(end=" ")
        for j in range(i) :
            print(upper[j],end=" ")
        for z in range(i, n+1) :
            print(end=" ")
        print(end="\n")
pattern17()



def pattern18() :
    n=int(input())
    for i in range(0,n) :
        for j in range(0,n) :
            if i == 0 or j==0 or i ==n-1 or j == n-1 :
                print("*",end="")
            else :
                print(end=" ")
        print()
pattern18()



def pattern19():
    row = int(input())
    for i in range(row) :
        for j in range(i+1) :
            print(1,end="")
        print()
pattern19()

"""


