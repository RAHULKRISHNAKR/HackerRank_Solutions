n,k= map(int, input().split())
scores = list(map(int, input().split()))

n = len(scores)

maxlist=[]

for i in range(n-k+1):
    window = scores[i:i+k]
    #maxlist.append(max(window))
    print(max(window), end=" ")

#print(maxlist)