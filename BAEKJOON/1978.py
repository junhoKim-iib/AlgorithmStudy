N = int(input())
check_list = map(int, input().split())

cnt = 0
def isPrime(num):
    global cnt

    if num < 2:
        return 

    for i in range(2, num):
        if num % i == 0:
            return 

    cnt += 1


for num in check_list:
    isPrime(num)

print(cnt)