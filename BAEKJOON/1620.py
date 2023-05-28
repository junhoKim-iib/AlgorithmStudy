import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    poketmon = input().rstrip()
    if poketmon.isdigit():
        print(dict[int(poketmon)])
    else:
        print(dict[poketmon])