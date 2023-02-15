N = int(input())
plan = input().split()

cur_loc = [1, 1]

for move in plan:
    if move == "L" and cur_loc[1] > 1:
        cur_loc[1] -= 1
    
    if move == "R" and cur_loc[1] < N:
        cur_loc[1] += 1
        
    if move == "U" and cur_loc[0] > 1:
        cur_loc[0] -= 1

    if move == "D" and cur_loc[0] < N:
        cur_loc[0] += 1


print(cur_loc)