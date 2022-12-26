# 6 - fro - to : 

def hanoi(fro, to, n):
    if n == 1:
        print(fro, to)
    else:
        hanoi(fro, 6-fro-to, n-1) 
        print(fro, to)
        hanoi(6-fro-to, to, n-1)


n = int(input())
times = 2**n - 1

if n <= 20:
    print(times)
    hanoi(1, 3, n)

else:
    print(times)
