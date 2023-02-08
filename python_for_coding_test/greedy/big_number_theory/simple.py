N, M, K = map(int, input().split())

nums = list(set(map(int, input().split())))

nums.sort(reverse= True)
first = nums[0]
second = nums[1]
cnt = 0
i = 0
res = 0

for _ in range(M):
    cnt += 1
    if cnt > K:
        i = 1
        cnt = 0

    res += nums[i]
    i = 0

print(res)
