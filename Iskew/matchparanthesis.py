'''Given an input of string in combinations of characters '{' and '}', which are parenthesis, you have to find if the input is balanced or not. The input is balanced if all the opening curly braces are closed. You can't close a curly brace before it is opened.'''
ip = input()

flag=0
c=0
for x in ip:
    if x=='{':
        flag=1
        c+=1
    elif x=='}':
        flag=0
        c-=1
if flag==0 and c==0:
    print("Matching")
else:
    print("Not Matching")