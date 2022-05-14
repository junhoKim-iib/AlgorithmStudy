

from signal import SIG_DFL


numbers =[2,7,11,15]
target = 9
result = []

def twoSum(numbers, target):
    l, r = 0, len(numbers) -1 
    while l < r:
        check = numbers[l] + numbers[r]
        if check == target:
           return [l + 1, r + 1]
           
        elif check < target:
            l += 1

        else: 
            r -= 1



result = twoSum(numbers, target)

print(result)