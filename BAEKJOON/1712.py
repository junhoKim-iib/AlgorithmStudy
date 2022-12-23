a, b, c = map(int, input().split())

if c <= b:
    print(-1)
    exit()

profit = c - b
n = a // profit + 1

print(n)