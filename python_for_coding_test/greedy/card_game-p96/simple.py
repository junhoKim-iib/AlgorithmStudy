N, M = map(int, input().split())    

min_list = []

for _ in range(N):
    temp = list(map(int, input().split()))  # input line by line
    min_list.append(min(temp)) # find min value in each line

print(max(min_list)) # find max value in min_list



