n = int(input())
arr = set(map(int, input().split()))
k = int(input())

count = 0

if k==0:
    from collections import Counter
    hashmap = Counter(arr)
    count = sum(i for val in hashmap if hashmap[val]>1)
else:
    for num in arr:
        if num+k in arr:
            count+=1  

print(count)  