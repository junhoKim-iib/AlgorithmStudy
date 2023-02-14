# N is size of array, M is number of times to add, K is number of times to add first number

N, M, K = map(int, input().split())

nums = list(set(map(int, input().split())))

nums.sort(reverse= True) # sort in descending order
first = nums[0] # biggerst number
second = nums[1] # second biggest number

big_cnt =  (M // (K+1) + M % (K+1)) * K # number of times to add first number
small_cnt = M - big_cnt # number of times to add second number

res = big_cnt * first  + small_cnt * second # sum of all numbers

print(res)

