n,k= map(int, input().split())
scores = list(map(int, input().split()))

n = len(scores)

windowsum = sum(scores[:k])
maxsum = windowsum

for i in range(k, n):
    windowsum += scores[i] - scores[i - k]
    maxsum = max(maxsum, windowsum)

print(maxsum)