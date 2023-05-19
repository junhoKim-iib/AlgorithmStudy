n = int(input())

nums = list(map(int, input().split()))

min, max = min(nums), max(nums)

print(min* max)