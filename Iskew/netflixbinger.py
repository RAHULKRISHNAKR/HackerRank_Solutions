n = int(input())
intervals = []
for _ in range(n):
    intervals.append(list(map(int, input().split())))

# Sort intervals by end time
intervals.sort(key=lambda x: x[1])

count = 1
end_time = intervals[0][1]
for i in range(1, n):
    if intervals[i][0] >= end_time:
        count += 1
        end_time