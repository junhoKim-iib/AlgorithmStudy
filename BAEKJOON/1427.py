n = int(input())

nums = list(map(int, str(n)))
nums.sort(reverse=True)
print(''.join(str(i) for i in nums))