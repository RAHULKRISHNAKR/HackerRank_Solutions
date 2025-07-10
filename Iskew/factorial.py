'''Write a program to find the factorial of a number using recursion.
'''

n = int(input())

def fact(n):
    f=0
    if n<1:
        f =1
    else:
        f = n*fact(n-1)
    return f

print(fact(n))
    