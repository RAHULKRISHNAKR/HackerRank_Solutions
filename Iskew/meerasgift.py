n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

miss = sum(a) - sum(b)

print(miss)