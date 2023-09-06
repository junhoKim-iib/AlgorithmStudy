def my_round(x): # 반올림 함수 
    if x - int(x) >= 0.5:
        return int(x) + 1
    elif x - int(x) < -0.5:
        return int(x) - 1
    else:
        return int(x)


import sys
input = sys.stdin.readline

n = int(input())

n_list = [0 for _ in range(8001)] # 배열 인덱스 사용 

for _ in range(n):
    n_list[int(input()) + 4000] += 1

# 산술평균
print(my_round(sum([(i - 4000) * n_list[i] for i in range(8001)]) / n))

existing_n_list = []
for i in range(8001):
    if n_list[i] != 0: # 인풋 값들 뽑아오기 
        existing_n_list += [i-4000] * n_list[i] # 카운팅 된 개수만큼 추가 
        
print(existing_n_list[len(existing_n_list) // 2] ) # 중앙값 

max_val_idx = n_list.index(max(n_list)) # 최빈값 인덱스 

if n_list.count(max(n_list)) == 1:# 최빈값이 하나라면 
    print(max_val_idx - 4000) # 그대로 출력 
else: # 여러개라면 
    n_list[n_list.index(max(n_list))] = 0 # 가장 작은 값 삭제
    print(n_list.index(max(n_list)) - 4000) # 두번째로 작은 값 출력 

# 범위 
print(existing_n_list[-1] - existing_n_list[0])