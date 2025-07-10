n =  int(input())
arr = list(map(str, input().split()))

hashmap={}

for i in arr:
    sorted_word = ''.join(sorted(i))
    if sorted_word in hashmap:
        hashmap[sorted_word].append(i)
    else:
        hashmap[sorted_word] = [i]

for key in hashmap:
    for v in hashmap[key]:
        print(v, end=' ')
    print()