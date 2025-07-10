'''Write a program that takes an array that denotes the daily closing prices of a stock to determine the maximum profit by buying and selling one share of the stock.'''
arr = list(map(int, input().split(',')))

bp = sp= arr[0]
p=0

for i in range(len(arr)):
    bp = min(bp,arr[i])
    sp = arr[i]
    p = max(p,sp-bp)

print(p)