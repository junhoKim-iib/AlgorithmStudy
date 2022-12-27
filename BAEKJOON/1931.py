n = int(input())
schedule = []
for _ in range(n):
    schedule.append(list(map(int, input().split())))


schedule.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0
for i in schedule:
    if i[0] >= end_time:
        count += 1
        end_time = i[1]

print(count)
