array = [[0 for col in range(100)] for row in range(100)]

n = int(input())

for i in range(n):
    left, bottom = map(int,input().split())
    for col in range(left-1,left+9):
        for row in range(100 - (bottom+10), 100 -bottom):
            array[row][col] = 1

res = 0
for i in array:
    res += i.count(1)
print(res)