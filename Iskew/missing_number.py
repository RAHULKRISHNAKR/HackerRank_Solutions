n = int(input())
arr = list(map(int, input().split()))

exsum = n * (n + 1) // 2
summ = sum(arr)

missing = exsum - summ

if missing == 0:
    if 0 in arr:
        print("Nothing's missing")
    else:
        print(0)
else:
    print(missing)