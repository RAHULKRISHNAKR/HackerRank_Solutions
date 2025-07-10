from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

hashmap = Counter(arr)

for room, count in hashmap.items():
    if count == 1:
        print(room)
        break