import sys
n = int(sys.stdin.readline().rstrip('\n'))

def factorial(n):
    res = 1
    for i in range(n, 1, -1):
        res = res * i
    return res

res = str(factorial(n))
cnt = 0
i = -1
while True:
    if res[i] == '0':
        cnt += 1
        i -= 1
    else:
        break

print(cnt)

